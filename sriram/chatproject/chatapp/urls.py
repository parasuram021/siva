from django.urls import path
from . import views

urlpatterns = [
    path('friend1/', views.friend1_chat, name='friend1'),
    path('friend2/', views.friend2_chat, name='friend2'),
]
