from django.contrib.auth.models import User, AbstractBaseUser, BaseUserManager
from django.db import models

class MyUserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not username:
            raise ValueError('Users must have an username')
        email = RacchaiUserManager.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password):
        return self.create_user(email, password)

class MyUser(AbstractBaseUser):
    name = models.CharField(max_length=12, unique=True)
    image = models.ImageField(upload_to='images/')
    USERNAME_FIELD = 'name'

    objects = MyUserManager()

    class Meta:
        db_table = 'racchai_user'
        swappable = 'AUTH_USER_MODEL'

class Tweet(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	text = models.TextField(max_length=144)
	time = models.DateTimeField('date published')
	def __str__(self):
		return self.text


# Create your models here.
