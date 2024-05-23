"""views for the AgriFund Project"""
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from .models import Project, LoanApplication, InvestorInterest
from .forms import InvestorInterestForm, ProjectForm, LoanApplicationForm

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
    interested_investors = project.investorinterest_set.all()

    form = InvestorInterestForm()

    if request.method == "POST":
        form = InvestorInterestForm(request.POST)
        if form.is_valid():
            investor_interest = form.save(commit=False)
            investor_interest.project = project
            investor_interest.save()
            return redirect('project_details', pk=pk)
    context = {'project': project, 'loan_applications': loan_applications,
            'interested_investors': interested_investors, 'form': form}

    return render(request, 'agri_project/project_details.html', context)

def project_create(request):
    """form to create and post a new agribusiness project"""
    form = ProjectForm()

    if request.method == "POST":
        form = ProjectForm(request.POST)
        if form.is_valid():
            project = form.save()
            return redirect(reverse('project_details', kwargs={'pk': project.pk}))
    else:
        form = ProjectForm()

    return render(request, 'agri_project/project_form.html', {'form': form})

def apply_loan(request):
    """renders loan application form"""
    form = LoanApplicationForm()
    if request.method == "POST":
        form = LoanApplicationForm(request.POST, request.FILES)
        if form.is_valid():
            loan = form.save()
            return redirect(reverse('project_details', kwargs={'pk': loan.project.pk}))
    return render(request, "agri_project/loan_form.html", {'form': form})

# Create your views here.
