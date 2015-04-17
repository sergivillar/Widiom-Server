# -*- coding: utf-8 -*-
from django.contrib import admin
from languages.models import Language, User_learns_language, User_knows_language

admin.site.register(Language)
admin.site.register(User_knows_language)
admin.site.register(User_learns_language)