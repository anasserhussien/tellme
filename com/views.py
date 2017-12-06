# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.contrib.auth.models import User
from .forms import MessageForm
from datetime import datetime
from .models import Message

# Create your views here.
RECEIVER_ID = 0
def index(request):

    try:
        received = Message.objects.filter(to_user =request.user)
    except:
        received = None
    try:
        sent = Message.objects.filter(from_user = request.user)
    except:
        sent = None

    return render(request, 'com/index.html',{'received':received, 'sent': sent})




def sending_message(request, name):
    send_complete = False
    try:
        User_obj = User.objects.get(username = name)
        RECEIVER_ID = User_obj.id
    except User.DoesNotExist:
        User_obj = None


    form = MessageForm()
    if request.method == 'POST':
        form = MessageForm(request.POST)
        if form.is_valid():
            message = form.save(commit = False)
            message.date = datetime.now()
            message.from_user = request.user
            message.to_user = User_obj
            message.save()
            send_complete = True

        else:
            print form.errors
    return render(request, 'com/viewing_user.html', {'form':form, 'u':name,'obj':User_obj, 'state':send_complete})
