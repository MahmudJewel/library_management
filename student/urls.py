from django.urls import path

from student import views

urlpatterns = [
	path('signup',views.signup, name='signup'),
	path('profile/<int:pk>', views.upadate_profile_view, name='profile'),
]