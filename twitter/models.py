from django.contrib.auth.models import User
from django.db import models
# class MyUser(User):

# 	def add_user(name, password):
# 		new_user=User(name=name,  password=password)
# 		new_user.save()

class Tweet(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	text = models.TextField(max_length=144)
	time = models.DateTimeField('date published')
	def __str__(self):
		return self.text


# Create your models here.
