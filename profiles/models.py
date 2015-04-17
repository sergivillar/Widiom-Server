# -*- coding: utf-8 -*-
from django.contrib.auth.models import User
from django.db import models
from django.conf import settings
from django.contrib.gis.db import models as gis_models
from django.contrib.gis import geos
from languages.models import Language
from profiles.settings import GENRES
from widiom.models import LocalizableModel


class Profile(LocalizableModel):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name=u'user', blank=True, null=True, editable=False)
    username = models.CharField(max_length=64)
    avatar = models.ImageField(upload_to='media', blank=True, null=True)
    born_date = models.DateField(blank=True, null=True)
    genre = models.CharField(max_length=3, choices=GENRES.items())
    last_time_localization = models.DateTimeField(auto_now_add=True)
    last_localization = gis_models.PointField(u"longitude/latitude", geography=True, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    language_read = models.ForeignKey(Language, blank=True, null=True) # Lenguaje en el que va a ver la aplicación

    def __unicode__(self):
        return unicode(self.username)
