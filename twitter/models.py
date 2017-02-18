from django.db import models

class User(models.Model):
	name = models.CharField(max_length=20)
	password = models.CharField(max_length=16)
	def __str__(self):
		return self.name

class Tweet(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	text = models.TextField(max_length=144)
	time = models.DateTimeField('date published')
	def __str__(self):
		return self.text


# Create your models here.
