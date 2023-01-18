from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns =[
    path('index/',views.jadenWebsite, name ='jadenSite'),
    path('alisite/',views.alisite, name ='alisite'),
    path('register/createData/', views.createData, name='createData'),
    path('register/', views.register, name='register'),
    #path('login/', views.login, name='login')
    path('', views.loginPage, name='login'),
    path('upload/', views.image_upload_view,name = 'upload'),
    path('userSite/', views.userSite, name='userSite'),
    path('profile/<str:pk>/', views.profile, name='profile')
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)