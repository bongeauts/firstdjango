# Freecad lib imported writing __init__.py file in each folder you want to import

import FreeCAD
import Part
import importWebGL


from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Box
from .serializers import BoxSerializer
from django.template import loader

def index(request):
    return HttpResponse("<h1>this is app1 homepage")


class BoxList(APIView):

    def get(self, request):
        Boxes = Box.objects.all()
        serializer = BoxSerializer(Boxes, many = True)
        return Response(serializer.data)

    def post(self):
        pass

def cube(request):
    template = loader.get_template('cube.html')
    context ={}
    return HttpResponse(template.render(context,request))

def createCube(request, pk):
    box_pk = Box.objects.get(pk=pk)
    doc = FreeCAD.newDocument("Unnamed1")
    doc.addObject("Part::Box", "Box")
    doc.ActiveObject.Label = "Cube"
    doc.recompute()
    FreeCAD.getDocument("Unnamed1").getObject("Box").Length = box_pk.boxLength
    FreeCAD.getDocument("Unnamed1").getObject("Box").Width = box_pk.boxWidth
    FreeCAD.getDocument("Unnamed1").getObject("Box").Height = box_pk.boxHeight
    doc.recompute()
    __objs__ = []
    __objs__.append(FreeCAD.getDocument("Unnamed1").getObject("Box"))
    importWebGL.export(__objs__, u"/home/luca/djangovenv2/website/app1/templates/cube1.html")
    template = loader.get_template('cube1.html')
    context = {}
    return HttpResponse(template.render(context, request))
