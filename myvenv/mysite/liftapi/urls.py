from django.urls import path
from . import views
from django.conf.urls import url,include
from django.contrib import admin
from .views import LiftViewSet
from rest_framework import routers


app_name = 'lift'

urlpatterns = [
    path('list/', views.lift_view, name = 'index'),
    path('total/', views.lift_list),
    path('liftdetail/<int:pk>/', views.lift_detail),
]
