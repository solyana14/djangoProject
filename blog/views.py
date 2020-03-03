from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

#handle request from homepage
#return what user wants to see

def home(request):
    return HttpResponse("<h1>blog home</h1>")#need to map this homepage to home url

def about(request):
    return HttpResponse("<h1>about blog</h1>")