# -*- coding: utf-8 -*-
from django.contrib.auth.models import User
from django.db import models


class Language(models.Model):
    name = models.CharField(max_length=255)
    icon = models.ImageField(upload_to='media')

    def __unicode__(self):
        return unicode(self.name)


class User_knows_language(models.Model):
    user = models.ForeignKey(User)
    language = models.ForeignKey(Language)
    votes = models.IntegerField(default=0)
    level = models.TextField()

    def __unicode__(self):
        return unicode(self.user) + u' - ' + unicode(self.language)


class User_learns_language(models.Model):
    user = models.ForeignKey(User)
    language = models.ForeignKey(Language)
    votes = models.IntegerField(default=0)
    level = models.TextField()

    def __unicode__(self):
        return unicode(self.user) + u' - ' + unicode(self.language)