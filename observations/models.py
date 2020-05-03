from django.contrib.gis.db import models
from django.contrib.auth.models import User
from django.contrib.humanize.templatetags.humanize import naturaltime
from datetime import date, datetime


# Create your models here.

class Site(models.Model):
    site_code = models.CharField(max_length=3, default='XXX', primary_key=True)
    site_name = models.CharField(max_length=50)
    site_description = models.TextField(max_length=225, null=True, blank=True)
    site_location = models.PointField()
    site_date_added = models.DateField()
    site_region_primary = models.CharField(max_length=50, null=True, blank=True)
    site_region_secondary = models.CharField(max_length=50, null=True, blank=True)
    external_link = models.CharField(max_length=255, null=True, blank=True)
    external_link_name = models.CharField(max_length=50, null=True, blank=True)
    
    def __str__(self):
        return self.site_name + " (" + self.site_code + ")"
        
    def current_vis(self):
        site = Observation.objects.filter(site=self.site_code).order_by('-when_observed')
        try:
            recent = ((datetime.now() - site[0].when_observed).days)<7
        except IndexError:
            recent = False

        try:
            return {"recent": str(recent), "obs1":{"Date": str(naturaltime(site[0].when_observed)),"Vis": site[0].visibility,"User": site[0].user.username},"obs2": {"Date": str(naturaltime(site[1].when_observed)),"Vis": site[1].visibility,"User": site[1].user.username},"obs3": {"Date": str(naturaltime(site[2].when_observed)),"Vis": site[2].visibility,"User": site[2].user.username}}
        except IndexError:
            try:
                return {"recent": str(recent), "obs1":{"Date": str(naturaltime(site[0].when_observed)),"Vis": site[0].visibility,"User": site[0].user.username},"obs2": {"Date": str(naturaltime(site[1].when_observed)),"Vis": site[1].visibility,"User": site[1].user.username},"obs3": {"Date": "No data ","Vis": "No data ","User": "No data "}}
            except IndexError:
                try:
                    return {"recent": str(recent), "obs1":{"Date": str(naturaltime(site[0].when_observed)),"Vis": site[0].visibility,"User": site[0].user.username},"obs2": {"Date": "No data ","Vis": "No data ","User": "No data "},"obs3": {"Date": "No data ","Vis": "No data ","User": "No data "}}

                except IndexError:
                    return {"recent": str(recent), "obs1":{"Date": "No data ","Vis": "No data ","User": "No data "},"obs2": {"Date": "No data ","Vis": "No data ","User": "No data "},"obs3": {"Date": "No data ","Vis": "No data ","User": "No data "}}
                
class Observation(models.Model):
    site = models.ForeignKey(Site, on_delete=models.CASCADE)
    when_observed = models.DateTimeField()
    conditions = models.CharField(max_length=225)
    visibility = models.IntegerField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    comments = models.CharField(max_length=225, null=True, blank=True)

    def __str__(self):
        return str(self.when_observed) +"_"+ self.site.site_name + "_by_"+ self.user.username
    
