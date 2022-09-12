from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from django.core.serializers import serialize
from django.http import HttpResponse
from .models import *

# Create your views here.

def HomePageView(request):

    context = {}
    return render(request, 'localise/index.html', context)

def county_datasets(request):
    counties = serialize('geojson', Counties.objects.all())
    return HttpResponse(counties, content_type='json')
