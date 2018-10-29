# -*- coding: utf-8 -*-
# Generated by Django 1.11.16 on 2018-10-23 11:51
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0025_remove_screenmodel_ticket_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='screenmodel',
            name='gold_seat',
            field=models.IntegerField(null=True, verbose_name='total gold Seats'),
        ),
        migrations.AddField(
            model_name='screenmodel',
            name='platinum_seats',
            field=models.IntegerField(null=True, verbose_name='total platinum Seats'),
        ),
        migrations.AddField(
            model_name='screenmodel',
            name='silver_seats',
            field=models.IntegerField(null=True, verbose_name='total silver Seats'),
        ),
    ]