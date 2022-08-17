from django.db import models
import logging
from datetime import datetime
logger = logging.getLogger(__name__)

# Weather Model is created
class Weather(models.Model):
    station = models.CharField(max_length=50, null=False, blank=False)
    date = models.DateField(null=False, blank=False)
    max_temp = models.FloatField(default=None, null=True, blank=True)
    min_temp = models.FloatField(default=None, null=True, blank=True)
    precipitation = models.FloatField(default=None, null=True, blank=True)

    def get_precipitation(self):
        return self.precipitation

    def __str__(self) -> str:
        return self.station+"--"+str(self.date)

    def save(self, *args, **kwargs):
        logger.warning("Starting Weather creation ")
        print(self.max_temp, self.min_temp,self.station,self.precipitation, self.date)
        if self.max_temp == -9999:
             self.max_temp = None
        if self.min_temp == -9999:
             self.min_temp = None
        # Weather.objects.update_or_create(station=self.station, date=self.date, defaults={'max_temp':self.max_temp, 'min_temp':self.min_temp, 'precipitation':self.precipitation}) 
        super(Weather, self).save(*args, **kwargs)

# Search results are stored
class search_results(models.Model):
    area_searched = models.CharField(null=True, blank=True, max_length=100)
    dt_stamp = models.DateTimeField(auto_now=True)
    year = models.CharField(null=True, blank=True, max_length=10)
    data = models.TextField(null=True, blank=True)

    def __str__(self) -> str:
        return f"{self.area_searched} searched on {self.dt_stamp}"

