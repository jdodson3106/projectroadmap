# Generated by Django 2.0.2 on 2018-02-28 12:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0018_task_in_work'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='clock_in',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='task',
            name='clock_out',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
