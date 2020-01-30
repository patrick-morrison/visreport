from django.contrib.gis import admin
from .models import Site, Observation

admin.site.register(Site, admin.OSMGeoAdmin)
admin.site.register(Observation, admin.OSMGeoAdmin)