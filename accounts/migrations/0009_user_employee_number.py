# Generated by Django 2.0 on 2018-01-29 16:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0008_remove_user_employee_number'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='employee_number',
            field=models.CharField(blank=True, default='', max_length=200, null=True),
        ),
    ]