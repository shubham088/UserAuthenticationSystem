from django.shortcuts import render
from django.urls import reverse
from django.http import HttpResponse
from django.contrib.auth.models import User


def accountsHomePage(request):
    return render(request, 'authenticationSystem/accountsHome.html', {})

def register(request):
    if request.method == 'GET':
        return render(request, 'authenticationSystem/register.html', {})
    else:
        first_name = request.POST['first-name']
        last_name = request.POST['last-name']
        email = request.POST['email']
        username = request.POST['username']
        pass1 = request.POST['password']
        pass2 = request.POST['password2']

        if pass1 == pass2:
            print("Both are correct password.")
            if not User.objects.filter(username = username).exists():
                user = User.objects.create_user(username=username, email=email, password=pass1, first_name=first_name, last_name=last_name)
                user.save()
                print("User created ")
                reverse('home')

    return render(request, 'authenticationSystem/register.html', {})


def login(request):
    return render(request, 'authenticationSystem/login.html', {})
