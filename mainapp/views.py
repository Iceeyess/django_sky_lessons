from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


# def index(request) -> HttpResponse:
#     print(request.POST)
#     print(f"type is {type(request)}")
#     if request.method == 'POST':
#         name = request.POST.get('name')
#         email = request.POST.get('email')
#         message = request.POST.get('message')
#         # print(f"{name} {email} {message}")
#     return render(request, 'main/index2.html')


def index(request) -> HttpResponse:

