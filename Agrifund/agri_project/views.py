"""views for the AgriFund Project"""
from django.shortcuts import render
from .models import Project

def landing_page(request):
    """renders the landing page"""
    return render(request, "agri_project/landing_page.html")

def project_listing(request):
    """renders the lists of agriprojects in Agrifund"""
    projects = Project.objects.all()
    context = {"projects": projects}
    return render(request, "agri_project/project_listings.html", context)

# Create your views here.
