from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from django.core.serializers import serialize
from django.http import HttpResponse
from .models import *

# Create your views here.

def HomePageView(request):

    context = {}
    return render(request, 'localise/index.html', context)

def countyData(request):
    counties = serialize('geojson', Counties.objects.all())
    return HttpResponse(counties, content_type='json')

def IncidenceData(request):
	points = serialize('geojson', Incidences.objects.all())
	return HttpResponse(points, content_type='json')
