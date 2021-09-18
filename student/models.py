from django.db import models
from datetime import datetime
from django.contrib.auth.models import User

# Create your models here.
class Student(models.Model):
	user=models.OneToOneField(User,related_name='profile', on_delete=models.CASCADE)
	birth_date = models.DateField(default=datetime.now)
	profile_pic= models.ImageField(default='student.png', upload_to='profile_pic/Student/',null=True,blank=True)
	address = models.CharField(max_length=50, null=True,blank=True)
	mobile = models.CharField(max_length=20,null=True,blank=True)

	@property
	def get_name(self):
		return self.user.first_name+" "+self.user.last_name
	@property
	def get_instance(self):
		return self
	def __str__(self):
 		return f'{self.user.username} Profile'