# Generated by Django 4.2.13 on 2024-06-16 05:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('getdata', '0005_rename_role_employee_default_role'),
    ]

    operations = [
        migrations.AddField(
            model_name='employee',
            name='role',
            field=models.CharField(default='', max_length=30),
            preserve_default=False,
        ),
    ]
