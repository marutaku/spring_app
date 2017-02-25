from django.conf.urls import url
from . import views
from django.contrib.auth.views import login,logout

app_name = 'twitter'
urlpatterns = [
    url(r'^$', login,{'template_name': 'twitter/login.html'}, name='login'),
    url(r'^signup/$', views.regist_user, name='signup'),
    url(r'^signup/thanks/$', views.login, name='thanks'),
    url(r'^index/$', views.IndexView.as_view(), name='index'),
    url(r'^logout/$', logout, name='logout')
    ]