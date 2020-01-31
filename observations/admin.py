from django.contrib import admin
from leaflet.admin import LeafletGeoAdmin
from .models import Site, Observation

admin.site.register(Site, LeafletGeoAdmin)
admin.site.register(Observation, LeafletGeoAdmin)