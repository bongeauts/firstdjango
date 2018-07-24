import sys
sys.path.append(0,'/user(lib/freecad/lib/')
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

class CreatePart(APIView):

    def get(self, request, pk):
        box_pk = Box.objects.get(pk=pk)
        doc = FreeCAD.newDocument()
        box_fc = doc.addObject("Part::Box","mybox")
        box_fc.Height = box_pk.boxHeight
        box_fc.Width = box_pk.boxWidth
        box_fc.Length = box_pk.boxLength