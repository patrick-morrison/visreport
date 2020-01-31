from django.shortcuts import render
from django.core.serializers import serialize
from .models import Site, Observation
from django.http import HttpResponse
from django.views import generic

# Create your views here.

def about(request):
    return render(request, 'observations/about.html')

def sites_view(request):
    points_as_geojson = serialize('geojson', Site.objects.all())
    return HttpResponse(points_as_geojson, content_type='json')

class MapView(generic.TemplateView):
    template_name = 'observations/map.html'
   
    def get_context_data(self):
        context = super(MapView, self).get_context_data()
        context['sites'] = Site.objects.all()
        return context