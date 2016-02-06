from django.template.loader import get_template
from django.template import Context
from django.shortcuts import render
from django.http import HttpResponse
import requests
import os
from django.contrib.auth.decorators import login_required

@login_required
def index(request):
    template = get_template('CoreActivityTracker/index.html')
    times = int(os.environ.get('TIMES',3))
    context = {
        'range_of_times_to_repeat': range(times),
    }
    return HttpResponse(template.render(context, request))
