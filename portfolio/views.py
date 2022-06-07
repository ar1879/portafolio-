from django.shortcuts import render
from . models import Project

# Create your views here.
def inicio(request):
    project = Project.objects.all()
    return render(request, 'portfolio/portfolio.html', {'project':project})