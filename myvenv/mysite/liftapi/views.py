from django.shortcuts import render
from .models import Lift

def lift_view(request):
    lifts = Lift.objects.all()
    return render(request,'index.html',{"lift" : lifts})

