from django.shortcuts import render
from django.http import HttpResponse
from mainapp.models import Student
from django.views.generic import ListView, DetailView

# Create your views here.


# class StudentListView(TemplateView):
#     model = Student
#     template_name = 'main/index3.html'


# def index(request) -> HttpResponse:
#     print(request.POST)
#     print(f"type is {type(request)}")
#     if request.method == 'POST':
#         name = request.POST.get('name')
#         email = request.POST.get('email')
#         message = request.POST.get('message')
#         # print(f"{name} {email} {message}")
#     return render(request, 'main/index2.html')

from django.views.generic import CreateView


class StudentsListView(ListView):
    template_name = 'main/index3.html'
    model = Student
    context_object_name = 'student_key'


class StudentDetailView(DetailView):
    model = Student
    template_name = 'main/student_detail.html'


def index(request) -> HttpResponse:
    student_list = Student.objects.all()
    objects_list = {
        'student_key': student_list,
        'greeting': 'Hello, World!'
    }
    return render(request, 'main/index3.html', objects_list)


def contact(request) -> HttpResponse:
    return render(request, 'main/contact.html')


def student_detail(request, student_id):
    student_resp = Student.objects.get(pk=student_id)
    d = {'student_resp': student_resp}
    return render(request, 'main/student_detail.html', d)

