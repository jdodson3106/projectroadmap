# Generated by Django 2.0 on 2018-01-16 12:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0002_project_company_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='project',
            name='company_name',
        ),
    ]
