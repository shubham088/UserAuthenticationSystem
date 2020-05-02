from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def accountsHomePage(request):
    return render(request, 'authenticationSystem/accountsHome.html', {})


def register(request):
    pass

def login(request):
    pass
