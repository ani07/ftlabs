import json
from django.core.management.base import BaseCommand
from Logs.models import *
from datetime import datetime
from dateutil import parser
from django.db import transaction

class Command(BaseCommand):

    def add_arguments(self, parser):
    	parser.add_argument('json_file', type=str)

    @transaction.atomic
    def handle(self, *args, **options):
        with open(options['json_file']) as f:
            data_list = json.load(f)

        for data in data_list['members']:
        	data['pk'] = data.pop('id')
        	created_by = 'System'
        	create_date = datetime.now()
        	User.objects.get_or_create(pk=data['pk'], real_name=data['real_name'], tz=data['tz'], 
        		create_date=create_date, update_date=create_date, created_by=created_by, updated_by=created_by)
        	for acts in data['activity_periods']:
        		st = parser.parse(acts['start_time'])
        		et = parser.parse(acts['end_time'])
        		ActivityPeriod.objects.get_or_create(user_id=data['pk'], start_time=st, end_time=et,
        			created_by=created_by , create_date=create_date , updated_by=created_by , update_date=create_date)