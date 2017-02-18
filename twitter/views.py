from django.shortcuts import render
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views import generic

def index(request):
	return render(request,'Twitter/index.html')
class signup:
	template_name = 'Twitter/sigup.html'
# Create your views here.
