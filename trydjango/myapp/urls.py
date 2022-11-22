from django.urls import path
from . import views

urlpatterns =[
    path('jadenSite/',views.jadenWebsite, name ='jadenSite'),
    #path('alisite/',views.alisite, name ='alisite'),
    path('register/createData/', views.createData, name='createData'),
    path('register/', views.register, name='register'),
    path('userSite/', views.userSite, name='userSite'),
    path('', views.loginPage, name='login')
]