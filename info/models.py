from django.db import models

# Create your models here.
Gender  = (
		('1', 'Male'), ('2', 'Female'),
	)
class District(models.Model):
	Name = models.CharField(max_length=100)
	Area = models.CharField(max_length=100)
	Population = models.CharField(max_length=100)

	def __str__(self):
		return self.Name

class UserInfo(models.Model):
	Name = models.CharField(max_length=100)
	Gender = models.CharField(choices = Gender, max_length= 100, default=1)
	Age = models.CharField(max_length=100)

	def __str__(self):
		return self.Name