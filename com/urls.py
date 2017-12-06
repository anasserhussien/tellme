from django.conf.urls import url, include
from django.contrib import admin
from com import views

app_name = 'com'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    #url(r'^(?P<name>[\w\-]+)/$',views.viewing_user, name='viewing_user'),
    url(r'^(?P<name>[\w\-]+)/send/$', views.sending_message, name='sending_message'),

]
