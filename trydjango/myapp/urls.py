from django.conf.urls.static import static
from django.urls import path
from . import views
from django.conf import settings

urlpatterns =[
    path('jadenSite/',views.jadenWebsite, name ='jadenSite'),
    path('register/createData/', views.createData, name='createData'),
    path('register/', views.register, name='register'),
    path('userSite/', views.userSite, name='userSite'),
    path('', views.loginPage, name='login'),
    path('changePfp', views.changePfp, name='changePfp')
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)