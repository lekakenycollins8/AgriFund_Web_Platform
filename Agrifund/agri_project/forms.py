"""script for model forms"""

from .models import InvestorInterest, Project, LoanApplication
from django import forms

class ProjectForm(forms.ModelForm):
    """creates form to fill agribusiness details"""

    STATUS_CHOICES = [
            ('Open', 'Open'),
            ('Closed', 'Closed'),
            ('Onhold', 'Onhold'),
            ]
    current_status = forms.ChoiceField(choices=STATUS_CHOICES)
    class Meta:
        model = Project
        fields = ['name', 'description', 'funding_goal', 'current_status',
                'farmer_name', 'farmer_email']
        widgets = {
                'name': forms.TextInput(attrs={'class': 'form-control'}),
                'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
                'funding_goal': forms.NumberInput(attrs={'class': 'form-control'}),
                'farmer_name': forms.TextInput(attrs={'class': 'form-control'}),
                'farmer_email': forms.EmailInput(attrs={'class': 'form-control'}),
                'current_status': forms.Select(attrs={'class': 'form-control'}),
                }

class InvestorInterestForm(forms.ModelForm):
    """inititalizes fields for investor details from investor model"""
    class Meta:
        model = InvestorInterest
        fields = ['investor_fname', 'investor_lname', 'investor_email',
                'amount_offered', 'interest_rate']
        widgets = {
                'investor_fname': forms.TextInput(attrs={'class': 'form-control'}),
                'investor_lname': forms.TextInput(attrs={'class': 'form-control'}),
                'investor_email': forms.EmailInput(attrs={'class': 'form-control'}),
                'amount_offered': forms.NumberInput(attrs={'class': 'form-control'}),
                'interest_rate': forms.NumberInput(attrs={'class': 'form-control'}),
                }

class LoanApplicationForm(forms.ModelForm):
    """creates Loan Application Form"""
    project = forms.ModelChoiceField(queryset=Project.objects.all(),
            label="Select Project",
            widget=forms.Select(attrs={'class': 'form-control'}))
    class Meta:
        model = LoanApplication
        fields = ['project', 'amount_requested', 'supporting_docs']
        widgets = {
            'amount_requested': forms.NumberInput(attrs={'class': 'form-control'}),
            'supporting_docs': forms.ClearableFileInput(attrs={'class': 'form-control'})
            }
