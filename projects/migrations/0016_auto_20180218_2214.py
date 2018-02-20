# Generated by Django 2.0.2 on 2018-02-18 22:14

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0015_auto_20180218_2208'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='assigned_to',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='task_assignee', to=settings.AUTH_USER_MODEL),
        ),
    ]
