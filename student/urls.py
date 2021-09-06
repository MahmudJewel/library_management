from django.urls import path

from student import views

urlpatterns = [
	path('signup',views.signup, name='signup'),
]