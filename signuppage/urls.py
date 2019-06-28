from django.urls import path
from . import views

urlpatterns = [
    path('ver/',views.verify,name='verify'),
    path('', views.index, name='index'),
]