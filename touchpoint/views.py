from django.shortcuts import render
import textwrap

from django.http import HttpResponse
from django.views.generic.base import View
from touchpoint.models import Touchpoint
 
from touchpoint.serializers import TouchpointSerializer

from rest_framework import generics
from rest_framework.response import Response
from rest_framework.reverse import reverse


class TouchpointList(generics.ListCreateAPIView):
    queryset = Touchpoint.objects.all()
    serializer_class = TouchpointSerializer
 
    def perform_create(self, serializer):
        serializer.save()
 
 
class TouchpointDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = TouchpointSerializer
 
    def get_queryset(self):
        return Touchpoint.objects.all()