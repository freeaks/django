from django.urls import path
from . import views

urlpatterns = [
    path('ver/',views.verify,name='verify'),
    path('doers/',views.doers,name='doers'),
    path('givers/', views.givers, name='givers'),
    path('', views.index, name='index'),
]