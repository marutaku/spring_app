from django.shortcuts import render
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views.decorators.http import require_POST
from django.views import generic
from django.contrib.auth.forms import UserCreationForm
from django.core.urlresolvers import reverse
#from .form import MakeUserForm
from django.contrib.auth.models import User
def index(request):
	return render(request,'twitter/index.html')
class Signup(generic.CreateView):
	model = User
	form_class = UserCreationForm
	template_name = 'twitter/signup.html'

	def get_success_url(self):
		return reverse('twitter:index')

@require_POST
def regist_save(request):
	form = MakeUserForm(request.POST)
	context= {
		'form': form,
	}
	return render(request, 'twitter/signup.html', context)
	#return render(request,'Twitter/signup.html')
# Create your views here.
