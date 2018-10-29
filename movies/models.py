# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.utils.translation import ugettext_lazy as _
from multiselectfield import MultiSelectField

# Create your models here.
INACTIVE = 0
ACTIVE = 1
STATUS = ((INACTIVE, 'Inactive'),(ACTIVE, 'Active'))


NONE='None'
MALAYALAM = 'Malayalam'
HINDI = 'Hindi'
ENGLISH = 'English'
TAMIL = 'Tamil'
ACTION='Action'
ADVENTURE='Adventure'
COMEDY='Comedy'
SCIENCE_FICTION='Science_Fiction'
CRIME='Crime'
DRAMA='Drama'
EPICS='Epic'
HORROR='Horror'
GENRE_CHOICES=((NONE, 'None'),(ACTION, 'action'),(ADVENTURE, 'adventure'),(COMEDY, 'comedy'),
	(SCIENCE_FICTION, 'science_fiction'),(CRIME, 'crime'),(DRAMA, 'drama'),(EPICS, 'epics'),(HORROR, 'horror'),)
LANGUAGE_CHOICES = ((NONE, 'None'),(MALAYALAM, 'M'),(HINDI, 'H'),(ENGLISH, 'E'),(TAMIL, 'T'),)



class MovieModel(models.Model):
	m_name=models.CharField(max_length=100,verbose_name='Movie Title',unique=True)
	m_language=models.CharField(max_length=20,verbose_name='Movie Language',choices=LANGUAGE_CHOICES,default=NONE)
	m_rating=models.DecimalField(max_digits=10,decimal_places=2,verbose_name='Movie IMDB Rating')
	m_genre=models.CharField(max_length=50,verbose_name='Movie Genre',choices=GENRE_CHOICES,default=NONE)
	m_length=models.DecimalField(max_digits=4,decimal_places=2,verbose_name='Movie length',help_text='enter time in hours')
	m_poster=models.ImageField(verbose_name='Movie Poster',upload_to='media/movie_posters')
	m_poster2=models.ImageField(verbose_name='Movie Poster cover',upload_to='media/movie_posters_covers',default='Pictures/ranam.jpg')
	m_trailer=models.FileField(verbose_name='Movie Trailer',upload_to='media/movie_trailers',blank='True')
	m_status= models.IntegerField(default=0, choices=STATUS,verbose_name='Movie Status')
	create_date=models.DateTimeField(auto_now=True)

	def __str__(self):
		return self.m_name

class ScreenModel(models.Model):
	sc_name=models.CharField(max_length=100,verbose_name='Screen name',blank=False,unique=True)
	silver_seats=models.IntegerField(verbose_name='total silver Seats',null=True)
	gold_seat=models.IntegerField(verbose_name='total gold Seats',null=True)
	platinum_seats=models.IntegerField(verbose_name='total platinum Seats',null=True)
	silver_price=models.IntegerField(verbose_name='silver Seat price',null=True)
	gold_price=models.IntegerField(verbose_name='gold Seat price',null=True)
	platinum_price=models.IntegerField(verbose_name='platinum seat price',null=True)
	sc_status= models.IntegerField(default=0, choices=STATUS,verbose_name='Screen Status')
	create_date=models.DateTimeField(auto_now=True)
	def __str__(self):
		return self.sc_name

class ShowModel(models.Model):
	s_date=models.DateField(blank=True,null=True)
	s_time=models.TimeField(blank=True,null=True)
	movie = models.ForeignKey(MovieModel,default='None')
	screen = models.ForeignKey(ScreenModel,default='None')
	s_status= models.IntegerField(default=0, choices=STATUS,verbose_name='Show Status')
	create_date=models.DateTimeField(auto_now=True)
	def __str__(self):
		return self.movie
class CarousalModel(models.Model):
	img_description=models.CharField(max_length=100,verbose_name='image description')
	img_carousal=models.ImageField(verbose_name='Home Carousal 1',upload_to='media/carousal')
	sc_status= models.IntegerField(default=0, choices=STATUS,verbose_name='Screen Status')
	create_date=models.DateTimeField(auto_now=True)
	def __str__(self):
		return self.img_description


