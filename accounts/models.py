# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _

# Create your models here.


INACTIVE = 0
ACTIVE = 1
STATUS = ((INACTIVE, 'Inactive'),(ACTIVE, 'Active'))

class Customer(models.Model):
     user_data = models.OneToOneField(User)
     u_ph_no = models.IntegerField()
     create_date=models.DateTimeField(auto_now=True)

     def __str__(self):
         return self.user_data

class Comment(models.Model):
	text = models.TextField(max_length=1000)
	created_at = models.DateTimeField(auto_now_add=True)

	class Meta:
		verbose_name = 'comment'
		verbose_name_plural = 'comments'