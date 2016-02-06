from django.conf.urls import url
from django.contrib.auth import views as django_auth_views
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^login/$', django_auth_views.login, name="my_login"),
]
