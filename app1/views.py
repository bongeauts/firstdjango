FREECADPATH = '/usr/lib/freecad/lib/'

import sys
sys.path.insert(0, FREECADPATH)
import FreeCAD

from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Box
from .serializers import BoxSerializer

def index(request):
    return HttpResponse("<h1>this is app1 homepage")

# Create your views here.
class BoxList(APIView):

    def get(self, request):
        Boxes = Box.objects.all()
        serializer = BoxSerializer(Boxes, many = True)
        return Response(serializer.data)

    def post(self):
        pass