from django.contrib import admin

# Register your models here.
from .models import Weather, search_results

admin.site.register(Weather)
admin.site.register(search_results)