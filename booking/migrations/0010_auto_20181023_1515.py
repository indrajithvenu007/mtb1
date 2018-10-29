# -*- coding: utf-8 -*-
# Generated by Django 1.11.16 on 2018-10-23 09:45
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0009_auto_20181023_1336'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reservationmodel',
            name='s_detail',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='movies.ShowModel'),
        ),
        migrations.AlterField(
            model_name='reservationmodel',
            name='user_data',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]