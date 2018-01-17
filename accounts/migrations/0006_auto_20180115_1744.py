# Generated by Django 2.0 on 2018-01-15 17:44

import accounts.models
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0005_auto_20180115_1500'),
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('user_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            bases=('accounts.user',),
            managers=[
                ('objects', accounts.models.UserManager()),
            ],
        ),
        migrations.AlterField(
            model_name='user',
            name='profile_image',
            field=models.ImageField(blank=True, default='static/images/profile-placeholder.png', null=True, upload_to='upload_pics/'),
        ),
        migrations.AddField(
            model_name='employee',
            name='boss',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='employee_boss', to=settings.AUTH_USER_MODEL),
        ),
    ]
