from CoreActivityTracker.models import SpokenLanguage
from rest_framework import serializers


class SpokenLanguageSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = SpokenLanguage
        fields = ('id', 'english_name', 'iso_639_2_code', 'iso_639_1_code', 'biblio_or_term')
