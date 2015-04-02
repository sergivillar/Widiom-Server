# -*- coding: utf-8 -*-
from django.contrib.auth.models import User
from django.db import models

from languages.models import User_knows_language


class Vote(models.Model):
    voter = models.ForeignKey(User)
    vote = models.BooleanField()
    timestamp = models.DateTimeField(auto_now_add=True)
    to_user_language = models.ForeignKey(User_knows_language)

    class Meta:
        unique_together = ('voter', 'to_user_language',)

    def __unicode__(self):
        return unicode(self.voter)