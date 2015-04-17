# -*- coding: utf-8 -*-
from widiom.settings.settings import *


DATABASES = {
    'default': {
        'ENGINE': 'django.contrib.gis.db.backends.postgis',
        'NAME': 'widiom',
        'USER': 'admin',
        'PASSWORD': 'admin'

    }
}
