from django.shortcuts import render
import socket

# Create your views here.
from django.http import HttpResponse


def index(request):
    try:
        hostname = socket.gethostname()
    except:
        hostname = 'localhost'
    return HttpResponse("Hostname: " + hostname)