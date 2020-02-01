from django.contrib.gis.db import models
from django.contrib.auth.models import User

# Create your models here.

class Site(models.Model):
    site_code = models.CharField(max_length=3, default='XXX', primary_key=True)
    site_name = models.CharField(max_length=50)
    site_description = models.TextField(max_length=225, null=True, blank=True)
    site_location = models.PointField()
    site_date_added = models.DateField()
    
    def __str__(self):
        return self.site_name + " (" + self.site_code + ")"
        
    def current_vis(self):
        site = Observation.objects.filter(site=self.site_code)
        return site.latest('when_observed').visibility

    def last_updated(self):
        site = Observation.objects.filter(site=self.site_code)
        return site.latest('when_observed').when_observed
        

class Observation(models.Model):
    site = models.ForeignKey(Site, on_delete=models.CASCADE)
    when_observed = models.DateTimeField()
    conditions = models.CharField(max_length=225)
    visibility = models.IntegerField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    comments = models.CharField(max_length=225, null=True, blank=True)

    def __str__(self):
        return str(self.when_observed) +"_"+ self.site.site_name + "_by_"+ self.user.username