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
        site = Observation.objects.filter(site=self.site_code).order_by('-when_observed')
        try:
            return {"obs1": {"Date":str(site[0].when_observed)[:16],"Vis":site[0].visibility}, "obs2": {"Date":str(site[1].when_observed)[:16],"Vis":site[1].visibility}, "obs3": {"Date":str(site[2].when_observed)[:16],"Vis":site[2].visibility}}
        except IndexError:
            try:
                return {"obs1": {"Date":str(site[0].when_observed)[:16],"Vis":site[0].visibility}, "obs2": {"Date":"No data","Vis":"No data"}, "obs3": {"Date":"No data","Vis":"No data"}}
            except IndexError:
                try:
                    return {"obs1": {"Date":str(site[0].when_observed)[:16],"Vis":site[0].visibility}, "obs2": {"Date":"No data","Vis":"No data"}, "obs3": {"Date":"No data","Vis":"No data"}}
                except IndexError:
                    return {"obs1": {"Date":"No data","Vis":"No data"}, "obs2": {"Date":"No data","Vis":"No data"}, "obs3": {"Date":"No data","Vis":"No data"}}
                
class Observation(models.Model):
    site = models.ForeignKey(Site, on_delete=models.CASCADE)
    when_observed = models.DateTimeField()
    conditions = models.CharField(max_length=225)
    visibility = models.IntegerField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    comments = models.CharField(max_length=225, null=True, blank=True)

    def __str__(self):
        return str(self.when_observed) +"_"+ self.site.site_name + "_by_"+ self.user.username
    
