from django.db import models


class User(models.Model):
    id = models.CharField(primary_key=True, max_length=50)
    real_name = models.CharField(max_length=200)
    tz = models.CharField(max_length=50, default='UTC')
    created_by = models.CharField(max_length=64, blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    updated_by = models.CharField(max_length=64, blank=True, null=True)
    update_date = models.DateTimeField(blank=True, null=True)



class ActivityPeriod(models.Model):
    id = models.AutoField(primary_key=True, )
    user = models.ForeignKey('User', models.DO_NOTHING)
    start_time = models.DateTimeField(blank=True, null=True)
    end_time = models.DateTimeField(blank=True, null=True)
    created_by = models.CharField(max_length=64, blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    updated_by = models.CharField(max_length=64, blank=True, null=True)
    update_date = models.DateTimeField(blank=True, null=True)
