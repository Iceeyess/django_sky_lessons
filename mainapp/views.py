from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin, UserPassesTestMixin
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


class StudentListView(LoginRequiredMixin, ListView):
    template_name = 'main/student_list.html'
    model = Student
    context_object_name = 'student_key'


class StudentUpdateView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    template_name = 'main/student_form.html'
    model = Student
    fields = ('first_name', 'last_name', 'avatar',)
    success_url = reverse_lazy('mainapp:student_list')
    permission_required = 'mainapp.change_student'


class StudentDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    template_name = 'main/student_confirm_delete.html'
    model = Student
    success_url = reverse_lazy('mainapp:student_list')

    def test_func(self):
        return self.request.user.is_superuser


class StudentDetailView(LoginRequiredMixin, PermissionRequiredMixin, DetailView):
    model = Student
    template_name = 'main/student_detail.html'
    permission_required = 'mainapp.view_student'


class StudentCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    model = Student
    fields = ('first_name', 'last_name', 'avatar' )
    # fields = '__all__'
    success_url = reverse_lazy('mainapp:student_list')
    template_name = 'main/student_form.html'
    permission_required = 'mainapp.add_student'



@login_required
@permission_required('mainapp.view_student')
def index(request) -> HttpResponse:
    student_list = Student.objects.all()
    objects_list = {
        'student_key': student_list,
        'greeting': 'Hello, World!'
    }
    return render(request, 'main/student_list.html', objects_list)


@login_required
def contact(request) -> HttpResponse:
    return render(request, 'main/contact.html')


@login_required
def student_detail(request, student_id):
    student_resp = Student.objects.get(pk=student_id)
    d = {'student_resp': student_resp}
    return render(request, 'main/student_detail.html', d)



@login_required
def toggle_activity(request, pk):
    student_item = get_object_or_404(Student, pk=pk)
    if student_item.is_active:
        student_item.is_active = False
    else:
        student_item.is_active = True
    student_item.save()
    return redirect(reverse('mainapp:student_list'))

