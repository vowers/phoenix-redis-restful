# -*- coding:utf-8 -*-
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import generics
from django.shortcuts import render
from .postdata import Postclient
from config import Config
import urllib

# Create your views here.
@api_view(['GET', 'POST'])
def get_list(request):
    if request.method == 'GET':        
        if request.GET.has_key('uuid'):
            return Response(request.GET['uuid'])
        else:                
            return Response(status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'POST':
        if request.POST.has_key('uuid'):
            urls = Config.redis_client_url
            post_data = Postclient()         
            uuid = request.POST['uuid']
            return Response(post_data.get_all_list(urls,uuid))
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)