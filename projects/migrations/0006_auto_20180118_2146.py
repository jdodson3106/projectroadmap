# Generated by Django 2.0 on 2018-01-18 21:46

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0005_auto_20180118_2145'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='deadline',
            field=models.DateTimeField(default=datetime.datetime(2018, 1, 18, 21, 46, 30, 432616)),
        ),
        migrations.AddField(
            model_name='project',
            name='start_date',
            field=models.DateTimeField(default=datetime.datetime(2018, 1, 18, 21, 46, 30, 432558)),
        ),
    ]