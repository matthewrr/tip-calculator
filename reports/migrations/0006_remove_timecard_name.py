# Generated by Django 4.2.13 on 2024-07-15 22:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reports', '0005_timecard_employee'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='timecard',
            name='name',
        ),
    ]
