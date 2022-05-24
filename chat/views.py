from email import message
from hashlib import new
from tokenize import Name
from unicodedata import name
from urllib import request
from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from django import http
from chat.models import Room, Message
import json
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout

# Create your views here.

#Génération d'une clé symétrique
#Key = Fernet.generate_key()
#Key_1 = Fernet(Key)

#Cette fonction renvoie la page HTML Home
def home(request):
    #return render(request, 'home.html')
    return render(request, 'home.html')

#Création de la salle 
def room(request, room):
    username = request.GET.get('username')

    #Reprend le nom utilisateur actuel
    username1 = request.user.get_username()

    #Création de la salle dans la Base de donnée
    room_details = Room.objects.get(name=room)

    #Retourne la page room.html avec l'association du dictionnaire des variables
    # qu'on pourra inclure directement dans le fichier HTML    
    return render(request, 'room.html',{
        'username': username,
        'username1' : username1,
        'room': room,
        'room_details': room_details
    })


#Vérification si la salle existe déjà ou pas
def checkview(request):
    room = request.POST['room_name']
    #username = request.POST['username']
    username = request.user.get_username()

    #Si l'objet du nom de la salle existe alors redirige vers la page avec room
    if Room.objects.filter(name=room).exists():
        return redirect('/'+room+'/?username='+username)
    
    #Sinon création de l'objet puis redirection vers la salle
    else:
        new_room = Room.objects.create(name=room)
        new_room.save()
        return redirect('/'+room+'/?username='+username)


#Cette fonction de sauvegarder le message en créant dans la table Message
def send(request):
    #Récupère la valeur des variables via la méthode POST
    message = request.POST['message'] 
    username = request.POST['username']
    room_id = request.POST['room_id']

    #Création des messages avec SQLite avec module python
    new_message = Message.objects.create(value=message, user=username, room=room_id)
    new_message.save()

    #print('Clé privé', Key_1)
    #Encrypt_Message = Key_1.encrypt(message) 
    #Decrypt_Message = Key_1.decrypt(Encrypt_Message) 
    #Decode_message = Decrypt_Message.decode()
    #new_crypt_message = 



#Récupération des messages pour chaques salles avec JSON
def getMessages(request, room):
    room_details = Room.objects.get(name=room)

    messages = Message.objects.filter(room=room_details.id)
    return JsonResponse({"messages":list(messages.values())})

#Création de la page d'enregistrement et les fonction
def signup(request):

    if request.method == "POST":
        #Récupération des valeurs via POST
        username = request.POST['username']
        name = request.POST['Name']
        last_name = request.POST['Last_Name']
        email = request.POST['Email']
        password = request.POST['password']
        c_password = request.POST['c_password']

        #Création de l'utilisateur
        myuser = User.objects.create_user(username, email, password)
        myuser.first_name = name
        myuser.last_name = last_name
        myuser.save()

        #Retourne la page success
        return render(request,"account_creation_success.html")

    return render(request, "signup.html")

def signin(request):
    
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']         

        user = authenticate(username=username, password=password)

        if user is not None:
            login(request, user)
            name = user.first_name
            return render(request, "CRYPTCHAT_CHAT.html", {'name': name} )
        
        else:
            return render(request,'login_error.html')

    return render(request, "signin.html")

def signout(request):
    logout(request)
    message.success(request, "Deconnexion réussi")
    return render(request,'CRYPTCHAT_CHAT.html')



