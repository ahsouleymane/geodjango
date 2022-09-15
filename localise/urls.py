from django.urls import path
from localise.views import *

urlpatterns = [
    path('', HomePageView, name="home"),
    path('county/', countyData, name="county"),
    path('incidence/', IncidenceData, name="incidence"),
    
]
