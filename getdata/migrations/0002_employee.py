# Generated by Django 4.2.13 on 2024-06-16 03:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('getdata', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=30)),
                ('last_name', models.CharField(max_length=30)),
                ('role', models.CharField(max_length=30)),
            ],
        ),
    ]
