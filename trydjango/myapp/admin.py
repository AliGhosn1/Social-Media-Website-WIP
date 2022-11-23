from django.contrib import admin
from .models import jadenSite ,SiteUsers,Post,Image

# Register your models here.
admin.site.register(jadenSite)
admin.site.register(SiteUsers)
admin.site.register(Post)
admin.site.register(Image)