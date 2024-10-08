# Generated by Django 4.2.13 on 2024-07-16 23:18

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reports', '0008_timecard_end_time_timecard_start_time'),
    ]

    operations = [
        migrations.AddField(
            model_name='report',
            name='tips_diff',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=6),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='timecard',
            name='end_time',
            field=models.DateTimeField(default=datetime.datetime(2024, 7, 16, 23, 18, 42, 64251, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='timecard',
            name='start_time',
            field=models.DateTimeField(default=datetime.datetime(2024, 7, 16, 23, 18, 42, 63950, tzinfo=datetime.timezone.utc)),
        ),
    ]
