from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return HttpResponse("type /rocky as suffix to continue")

def space(request):
    return HttpResponse("type /1 as suffix to continue")

def html(request):
    return render(request,"1.html")