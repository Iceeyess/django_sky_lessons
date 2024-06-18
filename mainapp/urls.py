from django.urls import path
from . import views
from .apps import MainappConfig

app_name = MainappConfig.name

urlpatterns = [
    path('', views.StudentListView.as_view(), name='index'),
    path('contact/', views.contact, name='contact')
]
