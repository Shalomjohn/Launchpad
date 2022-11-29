from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='index'),
    path('own', views.own, name='own')
]