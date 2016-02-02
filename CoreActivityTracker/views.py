from django.shortcuts import render
from django.http import HttpResponse
import requests
import os
from django.contrib.auth.decorators import login_required

@login_required
def index(request):
    times = int(os.environ.get('TIMES',3))
    return HttpResponse('Hello!' * times)
