from django.urls import path
from . import views

urlpatterns =[
    path('jadenSite/',views.jadenWebsite, name ='jadenSite'),
    path('alisite/',views.alisite, name ='alisite'),
    #path('',views.createWorkers, name ='create'),
    path('register/createData/', views.createData, name='createData'),
    path('register/', views.register, name='register'),
    #path('login/', views.login, name='login')
    path('', views.loginPage, name='login')
    ##sdasdasd
]