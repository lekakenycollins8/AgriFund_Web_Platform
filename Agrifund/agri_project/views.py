"""views for the AgriFund Project"""
from django.shortcuts import render, get_object_or_404
from .models import Project, LoanApplication

def landing_page(request):
    """renders the landing page"""
    return render(request, "agri_project/landing_page.html")

def project_listing(request):
    """renders the lists of agriprojects in Agrifund"""
    projects = Project.objects.all()
    context = {"projects": projects}
    return render(request, "agri_project/project_listings.html", context)

def project_details(request, pk):
    """details for a particular project based on id"""
    project = get_object_or_404(Project, pk=pk)
    loan_applications = project.loanapplication_set.all()
    context = {'project': project, 'loan_applications': loan_applications}

    return render(request, 'agri_project/project_details.html', context)

def project_create(request):
    """form to create and post a new agribusiness project"""
    return render(request, 'agri_project/project_form.html')

# Create your views here.
