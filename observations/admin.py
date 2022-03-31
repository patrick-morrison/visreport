from django.contrib import admin
from leaflet.admin import LeafletGeoAdmin
from .models import Site, Observation
from import_export.admin import ImportExportModelAdmin
from import_export import resources
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin

admin.site.register(Site, LeafletGeoAdmin)


class ObservationResource(resources.ModelResource):

    class Meta:
        model = Observation

class ObservationAdmin(ImportExportModelAdmin):
    resource_class =ObservationResource

admin.site.register(Observation,ObservationAdmin)

class UserResource(resources.ModelResource):
    class Meta:
        model = User

class UserAdmin(ImportExportModelAdmin, UserAdmin):
    resource_class = UserResource
    pass

admin.site.unregister(User)
admin.site.register(User, UserAdmin)