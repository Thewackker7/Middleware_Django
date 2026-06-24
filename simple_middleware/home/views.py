from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def home(request):
    return HttpResponse ("<h1> hi this is my website </h1>")
def myadmin(request):
    return HttpResponse ("<h1> hi this is my admin page </h1>")


