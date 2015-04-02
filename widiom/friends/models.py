# -*- coding: utf-8 -*-
from django.contrib.auth.models import User
from django.db import models
import datetime


class Friend(models.Model):
    friend_A = models.ForeignKey(User, related_name='friend_A')
    friend_B = models.ForeignKey(User, related_name='friend_B')
    blocked = models.BooleanField(default=False)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return unicode(self.friend_A) + u' - ' + unicode(self.friend_B)