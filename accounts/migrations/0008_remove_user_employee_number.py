# Generated by Django 2.0 on 2018-01-29 16:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0007_user_company_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='employee_number',
        ),
    ]