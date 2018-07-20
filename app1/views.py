from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("<h1>this is app1 homepage")

# Create your views here.
