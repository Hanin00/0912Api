from django.urls import path
from liftapi import views
from django.conf.urls import url,include
from django.contrib import admin


app_name = 'lift'

urlpatterns = [
    path('', views.lift_view, name = 'index'),
]