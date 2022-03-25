from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def dev(request):
    return HttpResponse("add paths to html page")
def index(request):
    return HttpResponse("app1/index.html")
def base(request):
    return HttpResponse("app1/base.html")
