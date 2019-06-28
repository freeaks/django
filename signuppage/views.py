from django.http import HttpResponse
from django.shortcuts import render
from .models import Users, Interests


def index(request):
    user=Users.objects.all()
    return render(request, 'index.html', )


def verify(request):
    return HttpResponse('Your account is created, now go to your email to verify it or put the code on your mobile phone')
