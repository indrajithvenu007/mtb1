# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from movies.models import ShowModel,ScreenModel
from accounts.models import User

# Create your models here.

class ReservationModel(models.Model):
	user_data = models.CharField(max_length=100,null=False)
	movie=models.CharField(max_length=100,null=False)
	screen=models.CharField(max_length=100,null=False)
	date=models.DateField(null=False)
	show_time=models.TimeField(null=False)
	ticket_class=models.CharField(max_length=20)
	# ticket_price_per_ticket= models.IntegerField(null=True)
	no_seats= models.IntegerField(blank=False)
	total_amt=models.DecimalField(max_digits=7,decimal_places=2,blank=False)
	create_date=models.DateTimeField(auto_now=True)
	def __str__(self):
		return self.user_data

 
