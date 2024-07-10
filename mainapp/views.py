from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from mainapp.models import Student
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy, reverse


# Create your views here.


# class StudentListView(TemplateView):
#     model = Student
#     template_name = 'main/student_list.html'


# def index(request) -> HttpResponse:
#     print(request.POST)
#     print(f"type is {type(request)}")
#     if request.method == 'POST':
#         name = request.POST.get('name')
#         email = request.POST.get('email')
#         message = request.POST.get('message')
#         # print(f"{name} {email} {message}")
#     return render(request, 'main/index2.html')


class StudentListView(ListView):
    template_name = 'main/student_list.html'
    model = Student
    context_object_name = 'student_key'


class StudentUpdateView(UpdateView):
    template_name = 'main/student_form.html'
    model = Student
    fields = ('first_name', 'last_name', 'avatar',)
    success_url = reverse_lazy('mainapp:student_list')


class StudentDeleteView(DeleteView):
    template_name = 'main/student_confirm_delete.html'
    model = Student
    success_url = reverse_lazy('mainapp:student_list')


class StudentDetailView(DetailView):
    model = Student
    template_name = 'main/student_detail.html'


class StudentCreateView(CreateView):
    model = Student
    fields = ('first_name', 'last_name', 'avatar' )
    # fields = '__all__'
    success_url = reverse_lazy('mainapp:student_list')
    template_name = 'main/student_form.html'

def index(request) -> HttpResponse:
    student_list = Student.objects.all()
    objects_list = {
        'student_key': student_list,
        'greeting': 'Hello, World!'
    }
    return render(request, 'main/student_list.html', objects_list)


def contact(request) -> HttpResponse:
    return render(request, 'main/contact.html')


def student_detail(request, student_id):
    student_resp = Student.objects.get(pk=student_id)
    d = {'student_resp': student_resp}
    return render(request, 'main/student_detail.html', d)


def toggle_activity(request, pk):
    student_item = get_object_or_404(Student, pk=pk)
    if student_item.is_active:
        student_item.is_active = False
    else:
        student_item.is_active = True
    student_item.save()
    return redirect(reverse('mainapp:student_list'))

