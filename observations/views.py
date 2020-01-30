from django.shortcuts import render

# Create your views here.

def map(request):
    return render(request, 'observations/map.html')

def about(request):
    return render(request, 'observations/about.html')