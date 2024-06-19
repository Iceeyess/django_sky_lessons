from django.shortcuts import render
from .models import Material
from django.views.generic import CreateView
from django.urls import reverse_lazy
# Create your views here.


class MaterialCreateView(CreateView):
    model = Material
    fields = ('title', 'description', )
    success_url = reverse_lazy('mainapp:index')