from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def App2_Funstion1(request):
    return HttpResponse("<h1>Hi i am function1 in app2</h1>")

def App2_Function2(request):
    return HttpResponse("<h1><i>Hi i am Function2 in app2")