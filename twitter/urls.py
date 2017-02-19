from django.conf.urls import url
from . import views

app_name = 'twitter'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^signup/$', views.Signup.as_view(), name='signup'),
    url(r'^signup/thanks$', views.index, name='thanks'),
]