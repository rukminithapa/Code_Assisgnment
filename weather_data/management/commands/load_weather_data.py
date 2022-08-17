#!/usr/bin/python
# -*- coding: utf-8 -*-
from hashlib import new
from django.core.management.base import BaseCommand
from django.utils import timezone
from assignment.settings import BASE_DIR
import os
import csv
from weather_data.models import Weather
from datetime import datetime
import logging
import pdb
logger = logging.getLogger(__name__)


class Command(BaseCommand):

    help = 'Loads weather data in DB.'

    def handle(self, *args, **kwargs):
        starttime = datetime.now()
        folder_path = str(BASE_DIR) + '/wx_data/'
        all_files = os.listdir(folder_path)
        (new_entry, updated) = ([], [])

        for each_file in all_files:
            if each_file.endswith('.txt'):
                with open(folder_path + each_file, 'r', encoding='utf8'
                          ) as weather_file:
                    tsv_reader = csv.reader(weather_file, delimiter='\t'
                            )
                    for row in tsv_reader:
                        (date_stamp, max_temp, min_temp,
                         precipitation) = row
                        date_stamp = datetime.strptime(date_stamp,
                                '%Y%M%d').date()
                        max_temp = (None if float(max_temp)
                                    == -9999 else float(max_temp) / 10)
                        min_temp = (None if float(min_temp)
                                    == -9999 else float(min_temp) / 10)
                        precipitation = float(precipitation) / 10
                        wthr = \
                            Weather.objects.filter(station=each_file[:
                                -4:], date=date_stamp)
                        if wthr.count() > 0:
                            wthr = wthr[0]
                            wthr.max_temp = max_temp
                            wthr.min_temp = min_temp
                            wthr.precipitation = precipitation
                            updated.append(wthr)
                        else:
                            new_entry.append(Weather(station=each_file[:
                                    -4:], date=date_stamp,
                                    max_temp=max_temp,
                                    min_temp=min_temp,
                                    precipitation=precipitation))
        Weather.objects.bulk_update(updated, ['max_temp', 'min_temp',
                                    'precipitation'], batch_size=10000)
        Weather.objects.bulk_create(new_entry, batch_size=10000)
        logger.info(f"Weather entries created : {len(new_entry)}. Entries Updated : {len(updated)}. Time taken : {datetime.now()-starttime}")
