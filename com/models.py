# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
from django.utils.encoding import python_2_unicode_compatible

class Profile (models.Model):

    user = models.OneToOneField(User, on_delete = models.CASCADE)
    bio = models.TextField(max_length= 500, blank=True)
    date_of_birth = models.DateField(blank=True, null = True)




class Message (models.Model):
    from_user = models.ForeignKey(User, related_name = 'message_sender')
    to_user = models.ForeignKey(User, related_name = 'messag_receiver')
    content = models.TextField(blank = False)
    date = models.DateTimeField(blank= True)
    def __str__(self):
        return self.content
