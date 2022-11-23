from django.db import models
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
# Create your models here.
import uuid
from datetime import datetime

class jadenSite(models.Model):
    name = models.CharField(max_length=255)
    title = models.CharField(max_length=255)

class SiteUsers(models.Model):
    name = models.CharField(max_length=255)
    picture = models.URLField(max_length=255, default="https://i.pinimg.com/736x/dd/f0/11/ddf0110aa19f445687b737679eec9cb2.jpg")

class Post(models.Model):
    id= models.UUIDField(primary_key=True,default=uuid.uuid4)
    user= models.CharField(max_length=100)
    image=models.ImageField(upload_to='post_images')
    #image = models.ImageField(upload_to='default/', blank=True, null=True, default='default.jpg')
    #caption=models.TextField()
    #created_at=models.DateTimeField(default=datetime.now)
    #no_of_likes=models.IntegerField(default=0)

    def __str__(self):
        return self.user

class Image(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    user = models.CharField(max_length=100)
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to='images')
    caption=models.TextField()

    def __str__(self):
        return self.user
