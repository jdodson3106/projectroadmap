# Generated by Django 2.0.2 on 2018-03-06 12:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0020_project_tz'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='tz',
            field=models.IntegerField(choices=[(0, 'CET'), (1, 'CST6CDT'), (2, 'Canada/Atlantic'), (3, 'Canada/Central'), (4, 'Canada/Eastern'), (5, 'Canada/Mountain'), (6, 'Canada/Newfoundland'), (7, 'Canada/Pacific'), (8, 'Canada/Saskatchewan'), (9, 'Canada/Yukon'), (10, 'Chile/Continental'), (11, 'Chile/EasterIsland'), (12, 'Cuba'), (13, 'UCT'), (14, 'US/Alaska'), (15, 'US/Aleutian'), (16, 'US/Arizona'), (17, 'US/Central'), (18, 'US/East-Indiana'), (19, 'US/Eastern'), (20, 'US/Hawaii'), (21, 'US/Indiana-Starke'), (22, 'US/Michigan'), (23, 'US/Mountain'), (24, 'US/Pacific'), (25, 'US/Pacific-New'), (26, 'US/Samoa'), (27, 'UTC'), (28, 'Universal')], default=0),
        ),
    ]
