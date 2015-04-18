# -*- coding: utf-8 -*-
from django.contrib.auth.models import User
from django.db import models
from django.contrib.gis.db import models as gis_models
from django.contrib.gis import geos
from languages.models import Language
from profiles.settings import GENRES


class Profile(models.Model):
    user = models.ForeignKey(User, null=True, blank=True)
    username = models.CharField(max_length=64)
    avatar = models.ImageField(upload_to='media', blank=True, null=True)
    born_date = models.DateField(blank=True, null=True)
    genre = models.CharField(max_length=3, choices=GENRES.items())
    last_time_localization = models.DateTimeField(auto_now_add=True)
    last_localization = gis_models.PointField(u"longitude/latitude", geography=True, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    language_read = models.ForeignKey(Language, blank=True, null=True) # Lenguaje en el que va a ver la aplicación

    # Filters
    filter_min_age = models.PositiveSmallIntegerField(blank=True, null=True)
    filter_max_age = models.PositiveSmallIntegerField(blank=True, null=True)
    filter_men = models.BooleanField(default=True)
    filter_women = models.BooleanField(default=True)
    filter_range = models.IntegerField(default=2500) # Distancia para buscar en metros

    def __unicode__(self):
        return unicode(self.username)
