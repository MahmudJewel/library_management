from django.shortcuts import render, redirect
from django.contrib.auth.models import Group
from django.contrib.auth.models import User
from django.contrib import messages
from django import forms
from flatpickr import DatePickerInput


from student import forms as SFORM
from student import models as SMODEL

# Create your views here.

def signup(request):
	RegisterForm = SFORM.RegisterForm()
	if request.method =='POST':
		RegisterForm = SFORM.RegisterForm(request.POST)
		if RegisterForm.is_valid():
			rform = RegisterForm.save()
			student_group=Group.objects.get_or_create(name='STUDENT')
			student_group[0].user_set.add(rform)
			username=RegisterForm.cleaned_data.get('username')
			#messages.warning(request, messages.error)
			messages.success(request, f"Account created for {username}")
			return redirect('login')
	context={
		'RegisterForm':RegisterForm,
	}

	return render (request, 'student/signup.html', context)


def upadate_profile_view(request, pk):
	user=SMODEL.User.objects.get(id=pk)
	student=SMODEL.Student.objects.get(id=pk)

	userForm=SFORM.EditForm(instance=user)
	studentForm = SFORM.studentForm(instance=student)

	if request.method == 'POST':
		userForm=SFORM.EditForm(request.POST, instance=user)
		studentForm = SFORM.studentForm(request.POST, request.FILES, instance=student) #profile is onetoonefield name
		#print(f"user id ={request.user.id} and profile id={request.user.profile.id}")
		#print(f"user ={request.user} and profile ={request.user.profile}")
		if userForm.is_valid() and studentForm.is_valid():
			userForm.save()
			studentForm.save()
			messages.success(request, f"Account has been updated")
			return redirect('/')
	context={
		'userForm':userForm,
		'studentForm':studentForm,
		'student':student
	}

	return render(request,'student/profile.html', context)