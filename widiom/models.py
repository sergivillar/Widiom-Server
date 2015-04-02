# -*- coding: utf-8 -*-
from django.db import models


class LocalizableModel(models.Model):
    lat = models.FloatField(editable=True, help_text='Latitude')
    lon = models.FloatField(editable=True, help_text='Longitude')