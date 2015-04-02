# -*- coding: utf-8 -*-
from django.contrib.auth.models import User
from django.db import models

from languages.models import Language

from profiles.settings import GENRES
from widiom.models import LocalizableModel


class Profile(LocalizableModel):
    user = models.ForeignKey(User)
    username = models.CharField(max_length=64)
    avatar = models.ImageField(upload_to='media')
    born_date = models.DateField(blank=True, null=True)
    genre = models.CharField(max_length=3, choices=GENRES.items())
    last_time_localization = models.DateTimeField(auto_now_add=True)
    description = models.TextField()
    language_read = models.ForeignKey(Language)

    def __unicode__(self):
        return unicode(self.username)
