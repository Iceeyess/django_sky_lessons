from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.shortcuts import render
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView

from users.forms import UserRegisterForm, UserProfileForm
from users.models import User


# Create your views here.


class LoginUserView(LoginView):
    template_name = 'users/login.html'
    form_class = AuthenticationForm


class LogoutUserView(LogoutView):
    pass


class RegisterUserView(CreateView):
    model = User
    form_class = UserRegisterForm
    template_name = 'users/register.html'
    success_url = reverse_lazy('users:login')


class ProfileUserView(UpdateView):
    model = User
    form_class = UserProfileForm
    success_url = reverse_lazy('users:profile')

    def get_object(self, queryset=None):
        return self.request.user
