# Generated by Django 4.2.13 on 2024-06-27 04:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0007_customuser_created_date_customuser_default_role_and_more'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Person',
        ),
    ]
