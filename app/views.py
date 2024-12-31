from django.shortcuts import render
from .models import Goal

# Create your views here.

def index(request):
    goals = Goal.objects.all()
    return render(request, "index.html", {"goals": goals})
