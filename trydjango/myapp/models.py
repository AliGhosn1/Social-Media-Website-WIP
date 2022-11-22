from django.db import models
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
# Create your models here.

class jadenSite(models.Model):
    name = models.CharField(max_length=255)
    title = models.CharField(max_length=255)

class SiteUsers(models.Model):
    name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    password = models.CharField(max_length=255)




