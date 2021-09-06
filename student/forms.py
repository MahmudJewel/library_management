from django import forms
from django.contrib.auth.models import User
from .models import student

class UserForm(forms.ModelForm):
    class Meta:
        model=User
        fields=['first_name','last_name','username','password']
        widgets = {
        'password': forms.PasswordInput()
        }

class StudentForm(forms.ModelForm):
    class Meta:
        model=student
        fields=['address','mobile','profile_pic']

