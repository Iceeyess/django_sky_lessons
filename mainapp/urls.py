from django.urls import path
from . import views
from .apps import MainappConfig


app_name = MainappConfig.name

urlpatterns = [
    path('', views.StudentsListView.as_view(), name='index'),
    path('contact/', views.contact, name='contact'),
    path('student/<int:pk>/', views.StudentDetailView.as_view(), name='student_detail'),
]
