# -*- coding:utf-8 -*-
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import generics
from django.shortcuts import render
from .getuserid import Getuserid
import urllib
# Create your views here.
@api_view(['GET', 'POST'])
def get_select(request):
 
    if request.method == 'GET':

        if request.GET.has_key('name'):
            userlist = Getuserid()
            return Response(userlist.getlist(request.GET['name']))
        else:               
            return Response(status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'POST':

        userlist = Getuserid()
        userlist = userlist.getlist(request.body)
        return Response(userlist)
        