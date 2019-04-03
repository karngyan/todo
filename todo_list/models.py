from django.db import models
from django.utils import timezone

class List(models.Model):
	item = models.CharField(max_length=200)
	completed = models.BooleanField(default=False)
	date_time = models.CharField(max_length=200)

	def __str__(self):
		return self.item + ' | ' + str(self.completed) + ' | ' + str(self.date_time)
