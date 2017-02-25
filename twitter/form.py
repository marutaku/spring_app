from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm
from django.forms import ModelForm
from .models import MyUser
from hashlib import sha1

class MakeUserForm(UserCreationForm):
    pass

class ProfileForm(forms.ModelForm):
    class Meta:
        model = MyUser
        fields = (
             'image','profile',
        )


class LoginForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['password'].widget.attrs['class'] = 'form-control'