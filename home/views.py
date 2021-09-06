from django.shortcuts import render, redirect
from django.contrib.auth.models import User

# Create your views here.

def home(request):
	if request.user.is_authenticated:
		redirect('signup')
	return render(request, 'home/home.html')
