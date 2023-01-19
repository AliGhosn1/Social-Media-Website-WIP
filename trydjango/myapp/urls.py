from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns =[
    path('register/', views.register, name='register'),
    path('', views.loginPage, name='login'),
    path('upload/', views.image_upload_view,name = 'upload'),
    path('profile/<str:pk>/', views.profile, name='profile')
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)