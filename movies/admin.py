# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from movies.models import MovieModel,ShowModel,ScreenModel,CarousalModel

# Register your models here.

admin.site.register(MovieModel)
admin.site.register(ShowModel)
admin.site.register(ScreenModel)
admin.site.register(CarousalModel)