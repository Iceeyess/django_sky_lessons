from django.urls import path
from . import views
from .apps import MainappConfig

app_name = MainappConfig.name

urlpatterns = [
    path('', views.StudentListView.as_view(), name='student_list'),
    path('contact/', views.contact, name='contact'),
    path('view/<int:pk>/', views.StudentDetailView.as_view(), name='view_student'),
    path('create/', views.StudentCreateView.as_view(), name='create_student'),
    path('edit/<int:pk>/', views.StudentUpdateView.as_view(), name='update_student'),
    path('delete/<int:pk>/', views.StudentDeleteView.as_view(), name='delete_student'),
    path('activity/<int:pk>/', views.toggle_activity, name='toggle_activity'),
]
