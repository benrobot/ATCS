from django.conf.urls import url, include
from django.contrib.auth import views as django_auth_views
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^login/$', django_auth_views.login, name="my_login"),

    #api
    url(r'^api/v1/spokenlanguages/$', 'views.spoken_language_collection'),
    url(r'^api/v1/spokenlanguages/(?P<pk>[0-9]+)$', 'views.spoken_language_element')
]
