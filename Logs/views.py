from datetime import datetime
from Logs.models import *
import json
from django.http import JsonResponse




def session_Logs(request):
	u_data = User.objects.all()
	a_data = ActivityPeriod.objects.all()
	members = []
	for users in u_data:
		member_dict = {'id':users.id, 'real_name':users.real_name, 'tz':users.tz}
		a_data = ActivityPeriod.objects.filter(user=users.id)
		time = []
		for act in a_data:
			start = act.start_time.strftime("%b %-d %Y %-I:%M%p")
			end = act.end_time.strftime("%b %-d %Y %-I:%M%p")
			act_dict = {'start_time':start, 'end_time':end}
			time.append(act_dict)
			member_dict['activity_periods'] = time
		members.append(member_dict)
	print(members)
	response_data = {}
	response_data['ok'] = 'true'
	response_data['members'] = members
	return JsonResponse(response_data)