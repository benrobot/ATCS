from django.shortcuts import render
from django.http import HttpResponse
import requests
import os


def index(request):
    times = int(os.environ.get('TIMES',3))
    return HttpResponse('Hello!' * times)
