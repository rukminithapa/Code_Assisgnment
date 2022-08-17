from django.views import View
from django.http import JsonResponse
import json
from weather_data.models import Weather
from yield_data.models import Yield
from rest_framework.decorators import api_view
from django.http import JsonResponse
from datetime import datetime
from django.core import serializers
from django.http import HttpResponse
from rest_framework import status
'''
Returns data from station code and date 
It shows weather details station code and date wise
'''
@api_view(['GET',])
def weather_details(request, station_code, date):
    try:
        date_stamp = datetime.strptime(date,
                                '%Y%M%d').date()
        data = Weather.objects.filter(station= station_code, date=date_stamp)
        post_list = serializers.serialize('json', data)
        return HttpResponse(post_list, content_type="text/json-comment-filtered")
    except Exception as exc:
        return JsonResponse({
            'message': "Error retrieving comments. :{}".format(str(exc))
            }, status= status.HTTP_500_INTERNAL_SERVER_ERROR)

'''
Returns data from year
It shows the year wise total yield
'''
@api_view(['GET',])
def yield_details(request, year):
    try:
        data = Yield.objects.filter(yr= year)
        post_list = serializers.serialize('json', data)
        return HttpResponse(post_list, content_type="text/json-comment-filtered")
    except Exception as exc:
        return JsonResponse({
            'message': "Error retrieving comments. :{}".format(str(exc))
            }, status= status.HTTP_500_INTERNAL_SERVER_ERROR)
        



