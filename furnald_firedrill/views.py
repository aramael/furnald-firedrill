__author__ = 'aramael'

from django.shortcuts import render
from furnald_firedrill.libs.firealarms.models import FireAlarm
def home(request):

    # Fetch Most Recent Verified Fire Alarm UTC
    most_recent_alarm = FireAlarm.objects.order_by('-alarm_date')[0]

    # Determine Current Time UTC
    import datetime
    from django.utils.timezone import utc
    now = datetime.datetime.utcnow().replace(tzinfo=utc)

    # Find Time Difference in Days
    time_difference = now - most_recent_alarm.alarm_date
    time_difference = str(time_difference.days)

    # Add Leading Zeros
    time_difference = "0"*(4-len(time_difference)) + time_difference

    context = {
        'days': time_difference
    }

    return render(request,'front_page.html', context)
