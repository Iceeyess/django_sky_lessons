from django.urls import path
from . import views
from .apps import MaterialsConfig



app_name = MaterialsConfig.name

urlpatterns = [
    path('create/', views.MaterialCreateView.as_view(), name='create'),
    # path('', ..., name='list'),
    # path('view/<int:pk>', ..., name='view'),
    # path('edit/<int:pk>', ..., name='edit'),
    # path('delete/<int:pk>', ..., name='delete'),

]
