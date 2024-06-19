from django.shortcuts import render
from django.http import HttpResponse
from mainapp.models import Student
from django.views.generic import ListView
# Create your views here.

class StudentListView(ListView):
    model = Student
    template_name = 'main/index.html'


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
    student_list = Student.objects.all()
    objects_list = {
        'student_key': student_list,
        'greeting': 'Hello, World!'
    }
    return render(request, 'main/index3.html', objects_list)


def contact(request) -> HttpResponse:
    return render(request, 'main/contact.html')

