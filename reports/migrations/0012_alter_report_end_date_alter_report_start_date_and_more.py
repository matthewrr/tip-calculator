# Generated by Django 4.2.13 on 2024-07-18 00:27

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reports', '0011_alter_timecard_end_time_alter_timecard_start_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='report',
            name='end_date',
            field=models.DateTimeField(default=datetime.datetime(2024, 7, 18, 0, 27, 20, 488398, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='report',
            name='start_date',
            field=models.DateTimeField(default=datetime.datetime(2024, 7, 18, 0, 27, 20, 488104, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='timecard',
            name='end_time',
            field=models.DateTimeField(default=datetime.datetime(2024, 7, 18, 0, 27, 20, 489347, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='timecard',
            name='start_time',
            field=models.DateTimeField(default=datetime.datetime(2024, 7, 18, 0, 27, 20, 489328, tzinfo=datetime.timezone.utc)),
        ),
    ]
