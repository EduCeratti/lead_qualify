from django.shortcuts import render
import textwrap

from django.http import HttpResponse
from django.views.generic.base import View
from touchpoint.models import Touchpoint
<<<<<<< HEAD
 
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
=======



class HomePageView(View):

    def dispatch(request, *args, **kwargs):
        response_text = textwrap.dedent('''\
            <html>
            <head>
                <title>Greetings to the world</title>
            </head>
            <body>
                <h1>Greetings to the world</h1>
                <p>Hello, world!</p>
            </body>
            </html>
        ''')

        #Touchpoint = Touchpoint()

        return HttpResponse(Touchpoint.objects.all().values())
>>>>>>> 0e2901b95ffb5790488b1fa33f7c9277b532c451
