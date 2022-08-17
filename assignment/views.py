from django.shortcuts import render
from django.http.response import HttpResponse
from weather_data.models import Weather
from yield_data.models import Yield
import logging
from assignment.constant import upload_search
logger = logging.getLogger(__name__)

'''
This method is to find avg max_temp for a year for a station code
The method takes the station code and year as argument
'''
def avg_max_temp(request, station_code, year):
    """This method is to find avg max_temp for a year for a area code"""
    try:
        objs = Weather.objects.filter(station= station_code, date__year=year)
        counter, total = 0, 0
        if objs.count() > 0:
            for obj in objs:
                if obj.max_temp is not None:
                    counter += 1
                    total += obj.max_temp
            msg = f"Avg value of max_temp for {station_code} for year {year} is : {total/counter} celsius"
            
        else:
            msg = "No data found. Please verify the station_code and year."
        return HttpResponse(msg)
    except Exception as exc:
        logger.error(str(exc))
    finally:
        upload_search("Business logic from avg_max_temp method",year, station_code)

'''
This method is to find avg min_temp for a year for a station code
The method takes the station code and year as argument
'''
def avg_min_temp(request,station_code, year):
    try:
        objs = Weather.objects.filter(station= station_code, date__year=year)
        counter, total = 0, 0
        if objs.count() > 0:
            for obj in objs:
                if obj.max_temp is not None:
                    counter += 1
                    total += obj.min_temp
            msg = f"Avg value for min_temp of {station_code} for year {year} is : {total/counter} celsius"
            
        else:
            msg = "No data found. Please verify the station_code and year."
        return HttpResponse(msg)
    except Exception as exc:
        logger.error(exc)
    finally:
        upload_search("Business logic from avg_min_temp method",year, station_code)
'''
This calculates the average precipitation
The function takes the station code and year as argument
This method is to find avg min_temp for a year for a area code
'''
def avg_precipitation(request,station_code, year):
    try:
        objs = Weather.objects.filter(station= station_code, date__year=year)
        counter, total = 0, 0
        if objs.count() > 0:
            for obj in objs:
                if obj.precipitation is not None:
                    counter += 1
                    total += obj.precipitation
            msg = f"Avg value for precipitation of {station_code} for year {year} is : {total/counter} cm"
        else:
            msg = "No data found. Please verify the station_code and year."
        return HttpResponse(msg)
    except Exception as exc:
        logger.error(str(exc))
    finally:
        upload_search("Business logic from avg_precipitation method",year, station_code)
