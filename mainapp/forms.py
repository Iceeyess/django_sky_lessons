from django import forms

from mainapp.models import Student

class StudentForm(forms.Form):

    class Meta:
        model = Student
        fields = ['first_name', 'last_name', 'avatar', 'email']
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
            'avatar': forms.FileInput(attrs={'class': 'form-control-file'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
                }


class SubjectForm(forms.Form):
    pass