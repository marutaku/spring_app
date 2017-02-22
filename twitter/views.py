from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views import generic
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from .models import Tweet
from .form import MakeUserForm, LoginForm
       
class Signup(generic.CreateView):
    model = User
    form_class = UserCreationForm
    template_name = 'twitter/signup.html'

    def get_success_url(self):
        return reverse('twitter:login')

@method_decorator(login_required, name='dispatch')
class IndexView(generic.ListView):
    template_name = 'twitter/index.html'
    context_object_name = 'latest_tweet_list'
    model = Tweet
    
    def get_queryset(self):
        return Tweet.objects.order_by('-time')[:50]


