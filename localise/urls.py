from django.urls import path
from localise.views import *

urlpatterns = [
    path('', HomePageView, name="home"),
    path('county_data/', county_datasets, name="county"),
    path('incidence_data/', HomePageView, name="home"),
    
]
