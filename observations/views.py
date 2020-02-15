import json
from django.http import JsonResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.core.serializers import serialize
from .models import Site, Observation
from django.http import HttpResponse
from django.views import generic


# Create your views here.

def about(request):
    return render(request, 'observations/about.html')

def sites_view(request):
    points_as_geojson = serialize('geojson', Site.objects.all())
    return JsonResponse(json.loads(points_as_geojson))

def reports_view(request):
    return JsonResponse(Observation.objects.all())

class MapView(generic.TemplateView):
    template_name = 'observations/map.html'
   
    def get_context_data(self):
        context = super(MapView, self).get_context_data()
        context['sites'] = Site.objects.all()
        return context

def detail(request, site_code):
    if request.method == 'POST':
            Observations = Observation()
            Observations.site = get_object_or_404(Site, pk=site_code)
            Observations.when_observed = request.POST['when_observed']
            Observations.conditions = request.POST['conditions']
            Observations.comments = request.POST['comments']
            Observations.visibility = request.POST['visibility']
            Observations.user = request.user
            Observations.save()
            return redirect("/"+str(Observations.site.site_code))
    else:
        site_code_up = site_code.upper()
        DiveSite = get_object_or_404(Site, pk=site_code_up)
        Observations = Observation.objects.all().filter(site=site_code_up).order_by('-when_observed')
        return render(request, 'observations/detail.html', {"Sites": DiveSite, "Observations":Observations})


def delete(request, pk):
        observation = get_object_or_404(Observation, pk=pk)
        if request.method == 'POST':
            observation.delete()
            return redirect("/"+str(observation.site.site_code))
        else:
            return redirect("/"+str(observation.site.site_code))