from django.db import models

# Create your models here.
class adminUser(models.Model):
	email=models.CharField(max_length=254,)
	password=models.CharField(max_length=100)
	cpassword=models.CharField(max_length=100)

	def __str__(self):
		return self.email