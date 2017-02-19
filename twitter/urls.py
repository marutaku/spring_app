from django.conf.urls import url
from . import views
from django.contrib.auth.views import login,logout

app_name = 'twitter'
urlpatterns = [
    url(r'^$', login,{'template_name': 'twitter/login.html'}, name='login'),
    url(r'^signup/$', views.Signup.as_view(), name='signup'),
    url(r'^signup/thanks/$', views.login, name='thanks'),
    url(r'^index/$', views.index, name='index')
    url(r'^logout/$', logout, name='logout')]