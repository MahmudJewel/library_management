from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from student.models import Student

@receiver (post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
	if created:
		try:
			print('created')
			Student.objects.create(user=instance) #Student objects will be created
		except:
			print('Not created')

@receiver (post_save, sender=User)
def save_profile(sender, instance, **kwargs):
	instance.profile.save() #profile is the OneToOneField name. see the Student model
