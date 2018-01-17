# Generated by Django 2.0 on 2018-01-13 01:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_user_organization'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='organization',
        ),
        migrations.AlterField(
            model_name='user',
            name='admin',
            field=models.BooleanField(default=True),
        ),
    ]
