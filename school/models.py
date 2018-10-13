from django.db import models

# Create your models here.
class SchoolInfo(models.Model):
	Name = models.CharField(max_length=100)
	Email = models.CharField(max_length=100)
	Phone = models.CharField(max_length=100)
	District = models.CharField(max_length=100)
	Address = models.TextField()
	Stablished_date = models.DateField()

	def __str__(self):
		return self.Name