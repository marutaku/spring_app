from django.contrib.auth.models import AbstractUser
from django.db import models
from django.contrib.auth.models import User


class MyUser(models.Model): 
    image = models.ImageField(upload_to='user_images', blank=True)
    profile = models.CharField(max_length=100)
    user = models.OneToOneField(User)
    def __str__(self):
        return self.name
    

class Tweet(models.Model):
    user = models.ForeignKey(MyUser, on_delete=models.CASCADE)
    text = models.TextField(max_length=144)
    time = models.DateTimeField('date published')
    def __str__(self):
        return self.text, self.user


# Create your models here.
