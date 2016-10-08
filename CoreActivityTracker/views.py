from django.template.loader import get_template
from django.template import Context
from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.http import HttpResponse
import requests
import os
from django.contrib.auth.decorators import login_required

from CoreActivityTracker.models import SpokenLanguage
from CoreActivityTracker.serializers import SpokenLanguageSerializer


@login_required
def index(request):
    template = get_template('CoreActivityTracker/index.html')
    times = int(os.environ.get('TIMES', 3))
    context = {
        'range_of_times_to_repeat': range(times),
    }
    return HttpResponse(template.render(context, request))


@api_view(['GET', 'POST'])
def spoken_language_collection(request):
    if request.method == 'GET':
        objects = SpokenLanguage.objects.all()
        serializer = SpokenLanguageSerializer(objects, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        data = {'text': request.DATA.get('the_spoken_language')}
        serializer = SpokenLanguageSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def spoken_language_element(request, pk):
    try:
        objects = SpokenLanguage.objects.get(pk=pk)
    except SpokenLanguage.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = SpokenLanguageSerializer(objects)
        return Response(serializer.data)
