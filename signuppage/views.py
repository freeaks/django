from django.http import HttpResponse
from django.shortcuts import render
from .models import Users


def index(request):
    return render(request, 'index.html', )


def doers(request):
    username = request.POST.get('username')
    full_name = request.POST.get('fullname')
    email = request.POST.get('email')
    password = request.POST.get('password')
    phone_number=request.POST.get('phonenumber')
    user=Users(username=username,full_name=full_name,email=email,password=password,phone_number=phone_number)
    print(user.password)
    #user.save()
    return render(request, 'doers.html',)


def givers(request):
    return render(request,'givers.html',)


def verify(request):
    return HttpResponse('Your account is created, now go to your email to verify it or put the code on your mobile phone')
