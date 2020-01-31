from django.shortcuts import render
from django.core.serializers import serialize
from .models import Site, Observation
from django.http import HttpResponse
from django.views.generic import TemplateView

# Create your views here.

def map(request):
    return render(request, 'observations/map.html')

def about(request):
    return render(request, 'observations/about.html')

def sites_view(request):
    points_as_geojson = serialize('geojson', Site.objects.all())
    return HttpResponse(points_as_geojson, content_type='json')

class MapView(TemplateView):
    template_name = 'observations/map.html'