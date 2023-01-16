from django.contrib import admin
from .models import jadenSite, SiteUsers, Image , Profile

# Register your models here.
admin.site.register(jadenSite)
admin.site.register(SiteUsers)
admin.site.register(Image)
admin.site.register(Profile)