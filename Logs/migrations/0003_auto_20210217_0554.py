# Generated by Django 3.1.6 on 2021-02-17 05:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Logs', '0002_auto_20210217_0544'),
    ]

    operations = [
        migrations.AlterField(
            model_name='activityperiod',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]