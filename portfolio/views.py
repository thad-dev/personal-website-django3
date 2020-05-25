from django.shortcuts import render

#TM imports
from .models import Project

# Create your views here.

def home(request):

    # Type is query set
    projects = Project.objects.all()

    return render(request, 'portfolio/home.html', {'projects': projects})