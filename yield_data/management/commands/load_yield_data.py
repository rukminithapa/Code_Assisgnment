#!/usr/bin/python
# -*- coding: utf-8 -*-
from hashlib import new
from django.core.management.base import BaseCommand
from django.utils import timezone
from assignment.settings import BASE_DIR
import os
import csv
from yield_data.models import Yield
from datetime import datetime
import logging
import pdb
logger = logging.getLogger(__name__)


class Command(BaseCommand):

    help = 'Loads weather data in DB.'

    def handle(self, *args, **kwargs):
        starttime = datetime.now()
        file_path = str(BASE_DIR) + '/yld_data/US_corn_grain_yield.txt'
        (new_entry, updated) = ([], [])


        with open(file_path, 'r', encoding='utf8'
                    ) as yield_file:
            tsv_reader = csv.reader(yield_file, delimiter='\t'
                    )
            for row in tsv_reader:
                (year, produce) = row

                wthr = \
                    Yield.objects.filter(yr=year)
                if wthr.count() > 0:
                    wthr = wthr[0]
                    wthr.qty = produce
                    updated.append(wthr)
                else:
                    new_entry.append(Yield(yr=year, qty = produce))
        Yield.objects.bulk_update(updated, ['qty'], batch_size=10000)
        Yield.objects.bulk_create(new_entry, batch_size=10000)
        logger.info(f"Yield entries created : {len(new_entry)}. Entries Updated : {len(updated)}. Time taken : {datetime.now()-starttime}")
