from django.urls import path
from . import views

#Dans cette liste, nous pouvons associer des view à l'URL du site.

urlpatterns = [
    path('', views.home, name='home'), #Utilise la fonction home dans le fichier views
    path('<str:room>/',views.room, name='room'),
    path('checkview',views.checkview, name='checkview'),
    path('send',views.send, name='send'),
    path('getMessages/<str:room>/',views.getMessages, name='getMessages'),
    path('signup',views.signup, name='signup'),
    path('signin',views.signin, name='signin'),
    path('signout',views.signout, name='signout'),
]
