from django.urls import path
from . import views
from .apps import MaterialsConfig



app_name = MaterialsConfig.name

urlpatterns = [
    path('create/', views.MaterialCreateView.as_view(), name='create'),
    path('', views.MaterialListView.as_view(), name='list'),
    path('view/<int:pk>/', views.MaterialDetailView.as_view(), name='view'),
    path('edit/<int:pk>/', views.MaterialUpdateView.as_view(), name='edit'),
    path('delete/<int:pk>/', views.MaterialDeleteView.as_view(), name='delete'),

]
