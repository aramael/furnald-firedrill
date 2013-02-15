from django.db import models

# Create your models here.
class FireAlarm(models.Model):

    alarm_date = models.DateTimeField()

    def __unicode__(self):
            return self.alarm_date.isoformat()

    class Meta:
        ordering = ['-alarm_date']