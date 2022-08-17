from django.test import TestCase, Client
from django.urls import reverse
import json
from rest_framework import status
from django.test.client import RequestFactory

# Create your tests here.

from django.test import TestCase
from .models import Weather

client = Client()
class WeatherTest(TestCase):
    """ Test module for Yield model """

    def setUp(self):
        Weather.objects.create(
            station='USC00110072',date='1985-01-03',max_temp='-6',min_temp='-106', precipitation='18')
        Weather.objects.create(
            station='USC00110187',date='1985-01-06',max_temp='-6',min_temp='-111', precipitation='20')
        self.factory = RequestFactory()

    '''
    Unit test the weather details
    '''
    def test_weather(self):
        weather_USC00110072 = Weather.objects.get(station='USC00110072')
        weather_USC00110187 = Weather.objects.get(station='USC00110187')
        self.assertEqual(
            weather_USC00110072.get_precipitation(), 18)
        self.assertEqual(
            weather_USC00110187.get_precipitation(), 20)

    '''
    Unit test the average max temperature details
    '''
    def test_avg_max_temp(self):
        response = self.client.get('http://127.0.0.1:8000/USC00110072/avg_max_temp/1985')
        print(response.status_code)
        self.assertEqual(response.status_code, 200)

    '''
    Unit test the average minimum temperature details
    '''

    def test_avg_min_temp(self):
        response = self.client.get('http://127.0.0.1:8000/USC00110072/avg_min_temp/1985')
        self.assertEqual(response.status_code, 200)

    '''
    Unit test the average precipitation details
    '''
    def test_avg_precipitation(self):
        response = self.client.get('http://127.0.0.1:8000/USC00110072/avg_precipitation/1985')
        self.assertEqual(response.status_code, 200)

    '''
     Unit test the total weather details
    '''
    def test_weather_details(self):
        response = self.client.get('http://127.0.0.1:8000/api/weather/USC00110072/19850109')
        self.assertEqual(response.status_code, 200)

    '''
    Unit test the total yield details
    '''
    def test_yield(self):
        response = self.client.get('http://127.0.0.1:8000/api/yield/2000')
        self.assertEqual(response.status_code, 200)