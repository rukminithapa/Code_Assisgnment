from django.db import models
import logging
from datetime import datetime
logger = logging.getLogger(__name__)

# Create your models here.
class Yield(models.Model):
    yr = models.IntegerField( null=False, blank=False,primary_key= True)
    qty = models.IntegerField(null=False, blank=False, default=0)

    def get_qty(self):
        return self.qty

    def __str__(self) -> str:
        return "Yield for year "+str(self.yr)