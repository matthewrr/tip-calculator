# Generated by Django 4.2.13 on 2024-06-18 19:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('getdata', '0008_employee_email_address_employee_phone_number'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='employee',
            name='role',
        ),
    ]
