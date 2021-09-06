from django.shortcuts import render, redirect
from django.contrib.auth.models import Group

from student import forms as SFORM
from student import models as SMODEL

# Create your views here.

def signup(request):
	userForm = SFORM.UserForm()
	studentForm = SFORM.StudentForm()
	if request.method=='POST':
		userForm=SFORM.UserForm(request.POST)
		studentForm=SFORM.StudentForm(request.POST, request.FILES)
		#print(userForm,studentForm)
		if userForm.is_valid() and studentForm.is_valid():
			user=userForm.save()
			user.set_password(user.password)
			user.save()
			student=studentForm.save(commit=False) #This doesn't save the form data immediately.wait for further changes.
			student.user=user
			student.save()
			student_group = Group.objects.get_or_create(name='STUDENT')
			student_group[0].user_set.add(user)
		return redirect('login')

	context={
		'studentForm':studentForm,
		'userForm' : userForm
	}

	return render (request, 'student/signup.html', context)


