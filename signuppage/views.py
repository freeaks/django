from django.http import HttpResponse
from django.shortcuts import render
from .models import Users


def index(request):
    return render(request, 'index.html', )


def doers(request):
    username = request.POST.get('username')
    fullname = request.POST.get('fullname')
    email = request.POST.get('email')
    password = request.POST.get('password')
    phonenumber=request.POST.get('phonenumber')
    user=Users(username=username,fullname=fullname,email=email,password=password,phonenumber=phonenumber)
    print(user.password)
    print(user.username)
    print(user.email)
    print(user.phonenumber)
    print(user.fullname)
    #user.save()
    return render(request, 'doers.html',)



def givers(request):
    return render(request,'givers.html',)


def verify(request):
    return HttpResponse('Your account is created, now go to your email to verify it or put the code on your mobile phone')
