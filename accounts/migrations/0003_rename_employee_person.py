# Generated by Django 4.2.13 on 2024-06-26 22:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_employee_username'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Employee',
            new_name='Person',
        ),
    ]
