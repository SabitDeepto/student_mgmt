from django.db import models

# Create your models here.
class Guardian(models.Model):
	Name = models.CharField(max_length=100)
	Relation = models.CharField(max_length=100)
	Gender_CHOICES = (('male', 'Male'), ('female', 'Female'))
	Gender = models.CharField(choices=Gender_CHOICES, max_length=50)
	age = models.IntegerField()
	phone = models.CharField(max_length=100, unique=True)

	def __str__(self):
		return self.Name


class Student(models.Model):
	name = models.CharField(max_length=100)
	roll = models.CharField(max_length=100)
	age = models.IntegerField()
	Gender_CHOICES = (('male', 'Male'), ('female', 'Female'))
	Gender = models.CharField(choices=Gender_CHOICES, max_length=50)
	guard = models.OneToOneField(Guardian, on_delete=models.SET_NULL, blank=True, null=True)

	def __str__(self):
		return self.name