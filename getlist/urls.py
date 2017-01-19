# -*- coding:utf-8 -*-
from django.conf.urls import  url
from . import views

urlpatterns = [
    url(r'^getlist/$', views.get_list, name='get_list'),

]