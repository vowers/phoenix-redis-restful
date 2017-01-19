# -*- coding:utf-8 -*-
from django.conf.urls import  url
from . import views

urlpatterns = [
    url(r'^phoenix/$', views.get_select, name='get_select'),

]