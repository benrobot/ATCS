"""ATCS URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import include, url
from django.contrib import admin
from login.views import *
from django.contrib.auth import views as django_auth_views
from rest_framework import routers
from CoreActivityTracker import urls as core_activity_tracker_urls

router = routers.DefaultRouter()
router.register(core_activity_tracker_urls.routers)

urlpatterns = [
    url(r'^$', django_auth_views.login, {'SSL': True}),
    url(r'^logout/$', logout_page, {'SSL': True}),
    url(r'^accounts/login/$', django_auth_views.login, {'SSL': True}), # If user is not login it will redirect to login page
    url(r'^register/$', register, {'SSL': True}),
    url(r'^register/success/$', register_success, {'SSL': True}),
    url(r'^home/$', home, {'SSL': True}),
    url(r'^(?i)CoreActivityTracker/', include('CoreActivityTracker.urls'), {'SSL': True}),
    url(r'^admin/', admin.site.urls, {'SSL': True}),
]
