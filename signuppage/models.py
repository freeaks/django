from django.db import models


class Users(models.Model):
    username = models.CharField(max_length=100,default='user')
    full_name = models.CharField(max_length=200)
    email = models.EmailField(max_length=200)
    password = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=10)


class Interests(models.Model):
    user = models.ForeignKey(Users, on_delete=models.CASCADE)
    interest= models.CharField(max_length=400)
