from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def App1_Funstion1(request):
    return HttpResponse("<h2>Hi i am Function1 in App1</h2>")

def App1_Function2(request):
    return HttpResponse("<marquee><h1>Hi i am Function2 in App1</h1></marquee>")

def App1_Function3(request):
    return HttpResponse("Hi i am Function3 in app1")