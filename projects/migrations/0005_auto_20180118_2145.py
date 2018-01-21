# Generated by Django 2.0 on 2018-01-18 21:45

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0007_user_company_name'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('projects', '0004_auto_20180117_1251'),
    ]

    operations = [
        migrations.AddField(
            model_name='feature',
            name='assigned_to',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='feature_assignee', to='accounts.Employee'),
        ),
        migrations.AddField(
            model_name='feature',
            name='owner',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='feature_owner', to=settings.AUTH_USER_MODEL),
        ),
    ]
