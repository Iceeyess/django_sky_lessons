from .apps import UsersConfig
from django.contrib import admin
from django.urls import path
from . import views

app_name = UsersConfig.name

urlpatterns = [
    path('login/', views.LoginUserView.as_view(), name='login'),
    path('logout/', views.LogoutUserView.as_view(), name='logout'),
    path('register/', views.RegisterUserView.as_view(), name='register'),
    path('profile/', views.ProfileUserView.as_view(), name='profile'),
]
