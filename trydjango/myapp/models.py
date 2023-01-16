from django.db import models
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
# Create your models here.
import uuid
from django.contrib.auth import get_user_model
from datetime import datetime
User = get_user_model()
class jadenSite(models.Model):
    name = models.CharField(max_length=255)
    title = models.CharField(max_length=255)

class SiteUsers(models.Model):
    name = models.CharField(max_length=255)
    picture = models.URLField(max_length=255, default="https://i.pinimg.com/736x/dd/f0/11/ddf0110aa19f445687b737679eec9cb2.jpg")

    def __str__(self):
        return self.name


class Profile(models.Model):
    user = models.OneToOneField(User, null=True, blank=True, on_delete=models.CASCADE)
    userId = models.IntegerField()
    userBio = models.TextField(blank=True)
    userProfileImg = models.ImageField(default="/blankpfp.jpg", null=True, blank=True)

    def __str__(self):
        return self.user.username


# class Post(models.Model):
#     id= models.UUIDField(primary_key=True,default=uuid.uuid4)
#     user= models.CharField(max_length=100)
#     image = models.ImageField(upload_to='static/images')
#     caption=models.TextField()
#
#     def __str__(self):
#         return self.user

class Image(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    user = models.CharField(max_length=100)
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to='images')
    caption=models.TextField(blank=True)

    def __str__(self):
        return self.user
