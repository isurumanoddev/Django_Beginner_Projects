from django.contrib import admin
from django.urls import path

from base import views

urlpatterns = [
    path('', views.home, name="home"),
    path('room/<str:pk>/', views.room, name="room"),
    path('create_room/', views.create_room, name="create-room"),
    path('update_room/<str:pk>/', views.update_room, name="update-room"),
    path('delete_room/<str:pk>/', views.delete_room, name="delete-room"),
    path('user_login/', views.user_login, name="login"),
    path('user_logout/', views.user_logout, name="logout"),
    path('user_register/', views.user_register, name="register"),
]
