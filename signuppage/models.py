from django.db import models


class Users(models.Model):
    username = models.CharField(max_length=100,default='user')
    fullname = models.CharField(max_length=200,default='fulln')
    email = models.EmailField(max_length=200,default='em')
    password = models.CharField(max_length=100,default='1234')
    phonenumber = models.CharField(max_length=10,default='120732')


class Interests(models.Model):
    user = models.ForeignKey(Users, on_delete=models.CASCADE)
    interest= models.CharField(max_length=400)
