from django.shortcuts import render

def landing_page(request):
    """renders the landing page"""
    return render(request, "agri_project/landing_page.html")
# Create your views here.
