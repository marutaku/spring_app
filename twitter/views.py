from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views import generic
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
       
class Signup(generic.CreateView):
    model = User
    form_class = UserCreationForm
    template_name = 'twitter/signup.html'

    def get_success_url(self):
        return reverse('twitter:login')

@login_required
class IndexView(generic.ListView):
    template_name = 'twitteer/index.html'
    context_name = 'latest_tweet_list'
    
    def get_queryset(self):
        return Tweet.objects.order_by('-time')[:50]

# Create your views here.
