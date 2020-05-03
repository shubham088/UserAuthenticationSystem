from django.shortcuts import render
from django.urls import reverse
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login

def accountsHomePage(request):
    return render(request, 'authenticationSystem/accountsHome.html', {})

def register(request):
    if request.method == 'GET':
        return render(request, 'authenticationSystem/register.html', {})
    else:
        first_name = request.POST.get('first-name')
        last_name = request.POST.get('last-name')
        email = request.POST.get('email')
        username = request.POST.get('username')
        pass1 = request.POST.get('password')
        pass2 = request.POST.get('password2')
        if pass1 == pass2:
            print("Both are correct password.")
            if not User.objects.filter(username = username).exists():
                user = User.objects.create_user(username=username, email=email, password=pass1, first_name=first_name, last_name=last_name)
                user.save()
                print("User created ")
                return HttpResponseRedirect(reverse('loginUser'))
        else:
            return render(request, 'authenticationSystem/register.html', {})



def loginUser(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        print("username : ", username)
        print("password : ", password)
        user = authenticate(username = username, password = password)
        if user is not None:
            login(request,user)
            print("login successfull")
            return HttpResponseRedirect(reverse('home'))
        else:
            print("check credentials")
            return render(request, 'authenticationSystem/login.html', {})
    else:
        return render(request, 'authenticationSystem/login.html', {})
