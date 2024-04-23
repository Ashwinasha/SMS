# students/forms.py
from django import forms
from .models import Student

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['student_id', 'name', 'address', 'age', 'date_of_birth', 'email']

from django.contrib.auth.forms import UserCreationForm


class RegistrationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        fields = ['username', 'password1', 'password2']
        help_texts = {
            'username': '',
        }
from django import forms

class LoginForm(forms.Form):
    username = forms.CharField(max_length=150)
    password = forms.CharField(widget=forms.PasswordInput)
