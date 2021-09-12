from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from .models import Lift

def lift_view(request):
    lifts = Lift.objects.all()

# return render(request,'index.html',{"lift" : lifts})
    return render(request,'index.html',{'lifts' : lifts})

