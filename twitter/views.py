from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views import generic
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from .models import Tweet
from .form import MakeUserForm, LoginForm, ProfileForm
from django.utils import timezone

def regist_user(request):
    user_form = MakeUserForm(request.POST or None)
    profile_form = ProfileForm(request.POST or None, request.FILES)
    if request.method == "POST" and user_form.is_valid() and profile_form.is_valid():

        # Userモデルの処理。ログインできるようis_staffをTrueにし保存
        user = user_form.save(commit=False)
        user.is_staff = True
        user.save()

        # Profileモデルの処理。↑のUserモデルと紐づけましょう。
        profile = profile_form.save(commit=False)
        profile.user = user
        profile.save()

        login(
            request, user, backend="django.contrib.auth.backends.ModelBackend")

        return redirect("twitter:index")

    context = {
        "user_form": user_form,
        "profile_form": profile_form,
    }
    return render(request, 'twitter/signup.html', context)

@method_decorator(login_required, name='dispatch')
class IndexView(generic.ListView):
    template_name = 'twitter/index.html'
    context_object_name = 'latest_tweet_list'
    model = Tweet

    def get_queryset(self):
        return Tweet.objects.order_by('-time')[:50]


def tweet_add(request):
    user_now = request.user
    tweeting = user_now.tweet_set.create(
                text = request.POST["text"],
                time = timezone.now())
    tweeting.save()
    return redirect("twitter:index")


class DetailView(generic.DetailView):
    model = User
    template_name = 'twitter/detail.html'


def tweet_delete(request):
    tweet_id = request.POST["id"]
    target_tweet = Tweet.objects.get(pk=tweet_id)
    user_id = target_tweet.user_id
    if request.user.id == user_id:
        target_tweet = Tweet.objects.get(pk=tweet_id)
        target_tweet.delete()
    else:
        print("missmatch")
    return redirect("twitter:index")

def favorit_add(request):
    tweet_id = request.POST["id"]
    target_tweet = Tweet.objects.get(pk=tweet_id)
    target_tweet.fav = target_tweet.fav + 1
    target_tweet.save()
    return redirect("twitter:index")