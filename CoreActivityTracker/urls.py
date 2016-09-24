from django.conf.urls import url, include
from django.contrib.auth import views as django_auth_views
from rest_framework import routers, viewsets
from . import views, serializers, models


# ViewSets define the view behavior.
class SpokenLanguageViewSet(viewsets.ModelViewSet):
    queryset = models.SpokenLanguage.objects.all()
    serializer_class = serializers.SpokenLanguageSerializer

# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register(r'SpokenLanguages', SpokenLanguageViewSet)

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^login/$', django_auth_views.login, name="my_login"),
    url(r'^api/', include(router.urls)),
    url(r'^apidoc/', include('rest_framework.urls', namespace='rest_framework'))
]
