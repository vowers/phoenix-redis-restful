# -*- coding:utf-8 -*-
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import generics
from django.shortcuts import render
from .select import SelectDB


# Create your views here.
@api_view(['GET', 'POST'])
def get_select(request):

    if request.method == 'GET':
        if request.GET.has_key('sql'):
            test = SelectDB()
            return Response(
                test.get_select(request.GET['sql']),
                status=status.HTTP_201_CREATED)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'POST':

        if request.POST.has_key('sql'):
            test = SelectDB()
            return Response(
                test.get_select(request.POST['sql']),
                status=status.HTTP_201_CREATED)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)