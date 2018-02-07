# -*- coding: utf-8 -*-
# Generated by Django 1.9.3 on 2016-04-23 02:08
from __future__ import unicode_literals

from django.db import migrations, models
import scanner.models


class Migration(migrations.Migration):

    dependencies = [
        ('scanner', '0003_auto_20160421_1914'),
    ]

    operations = [
        migrations.AddField(
            model_name='scanresult',
            name='mac',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='scanresult',
            name='os',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='job',
            name='status',
            field=models.CharField(choices=[('P', 'Pending'), ('E', 'Executing'), ('R', 'Retry'), ('K', 'Killed'), ('C', 'Complete'), ('H', 'Hold')], default='P', editable=False, max_length=1),
        ),
        migrations.AlterField(
            model_name='scan',
            name='status',
            field=models.CharField(choices=[('P', 'Pending'), ('S', 'Setting up'), ('R', 'Running'), ('C', 'Complete'), ('H', 'On Hold')], default='R', max_length=1),
        ),
        migrations.AlterField(
            model_name='scanner',
            name='name',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='scanner',
            name='token',
            field=models.CharField(default=scanner.models.generate_random_password, max_length=256),
        ),
        migrations.AlterField(
            model_name='scanresult',
            name='ip',
            field=models.CharField(blank=True, max_length=15, null=True),
        ),
    ]
