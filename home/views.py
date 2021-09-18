from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages

# Create your views here.

def home(request):
	if request.user.is_authenticated:
		redirect('afterlogin')
	messages.warning(request, messages.error)
	return render(request, 'home/home.html')

def is_student(user):
    return user.groups.filter(name='STUDENT').exists()

def afterlogin_view(request):
	if is_student(request.user):
		return redirect('/')
	else:
		return render (request, 'admn/test.html')
