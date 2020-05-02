from django.shortcuts import render
from django.http import HttpResponse


def firstPage(request):
    return HttpResponse("Go to /home")
