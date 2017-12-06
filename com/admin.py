# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import Message
from django.contrib.auth.models import User

class MessageAdmin(admin.ModelAdmin):
    list_display = ('from_user','to_user','content','date')

admin.site.register(Message, MessageAdmin)
#admin.site.register(User)
# Register your models here.
