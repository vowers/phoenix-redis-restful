# -*- coding:utf-8 -*-
from django.conf.urls import  url
from . import views

urlpatterns = [
    url(r'^getredis/$', views.get_select, name='get_select'),

]