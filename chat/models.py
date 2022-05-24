from datetime import datetime
from django.db import models


#Création d'une TABLE SQL via python django
class Room(models.Model):
    name = models.CharField(max_length=1000)

class Message(models.Model):
    value = models.CharField(max_length=1000000)
    date = models.DateTimeField(default=datetime.now, blank=True)
    user = models.CharField(max_length=1000000)
    room = models.CharField(max_length=1000000)



#class Username(models.Model):
#    Username = models.CharField(max_length=100000)
#    Password = models.CharField(max_length=64)