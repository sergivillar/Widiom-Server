# -*- coding: utf-8 -*-
from django.db import models


class Regist(models.Model):
    email = models.EmailField()
    username = models.CharField(max_length=64)
    password = models.CharField(max_length=128)
    encrypt = models.CharField(max_length=128)
    activate = models.BooleanField(default=False)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return unicode(self.email)