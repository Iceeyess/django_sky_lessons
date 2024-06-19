from django.urls import path
from . import views
from .apps import MainappConfig


app_name = MainappConfig.name

urlpatterns = [
    path('', views.index, name='index'),
    path('contact/', views.contact, name='contact'),
    path('student/<int:student_id>', views.student_detail, name='student_detail'),
]
