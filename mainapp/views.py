from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin, UserPassesTestMixin
from django.core.cache import cache
from django.forms import inlineformset_factory
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse

from config import settings
from mainapp.forms import SubjectForm
from mainapp.models import Student, Subject
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

    def get_success_url(self, *args, **kwargs):
        return reverse('main:students_update', args=[self.get_object().pk])






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

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        if settings.CACHE_ENABLED:
            key = f'subject_list_{self.object.pk}'
            subject_list = cache.get(key)
            if subject_list is None:
                subject_list = self.object.subject_set.all()
                cache.set(key, subject_list)
        else:
            subject_list = self.object.subject_set.all()

        context_data['subject_list'] = subject_list
        return context_data


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

