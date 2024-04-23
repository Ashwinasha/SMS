# students/views.py
from django.shortcuts import render, redirect, get_object_or_404
from .models import Student
from .forms import StudentForm

def student_list(request):
    students = Student.objects.all()
    return render(request, 'students/student_list.html', {'students': students})

# views.py
from django.shortcuts import render, redirect
from .models import Student

def student_create(request):
    if request.method == 'POST':
        student_id = request.POST.get('student_id')
        name = request.POST.get('name')
        age = request.POST.get('age')
        email = request.POST.get('email')
        dob = request.POST.get('date_of_birth')  # Corrected field name
        address = request.POST.get('address')
        
        # Create a new student object and save it to the database
        student = Student(student_id=student_id, name=name, age=age, email=email, date_of_birth=dob, address=address)  # Corrected field name
        student.save()
        
        # Redirect to the student list page after saving the student
        return redirect('student_list')
    
    # Render the form template for GET requests
    return render(request, 'students/student_form.html')



def student_detail(request, pk):
    student = get_object_or_404(Student, pk=pk)
    return render(request, 'students/student_detail.html', {'student': student})

def student_edit(request, pk):
    student = get_object_or_404(Student, pk=pk)
    if request.method == 'POST':
        form = StudentForm(request.POST, instance=student)
        if form.is_valid():
            form.save()
            return redirect('student_list')
    else:
        form = StudentForm(instance=student)
    return render(request, 'students/student_edit.html', {'form': form})


def student_delete(request, pk):
    student = get_object_or_404(Student, pk=pk)
    if request.method == 'POST':
        student.delete()
        return redirect('student_list')
    return render(request, 'students/student_confirm_delete.html', {'student': student})

# views.py
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect

from django.shortcuts import render, redirect
from .forms import RegistrationForm

def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')  # Redirect to login page after successful registration
    else:
        form = RegistrationForm()  # Pass None here instead of 'student_list'
    
    # If the form submission failed, pass the form instance with errors back to the template
    return render(request, 'students/register.html', {'form': form})





from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class RegistrationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User
        fields = ['username', 'password1', 'password2']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['password1'].widget = forms.PasswordInput(attrs={'placeholder': 'Password'})
        self.fields['password2'].widget = forms.PasswordInput(attrs={'placeholder': 'Confirm Password'})

    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Passwords do not match")
        return password2


from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from .forms import LoginForm

def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                # Redirect to the appropriate page after login
                return redirect('student_create')
            else:
                # Authentication failed, display an error message
                print("Authentication failed: Invalid username or password.")  # Debug statement
                form.add_error(None, "Invalid username or password.")
        else:
            print("Form is invalid.")  # Debug statement
    else:
        form = LoginForm()
    return render(request, 'students/login.html', {'form': form})




def user_logout(request):
    logout(request)
    return redirect('login')

def home(request):
    return render(request, 'students/home.html')