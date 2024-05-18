"""Models for the AgriFund Web Platform"""

from django.db import models

class BaseModel(models.Model):
    """basemodel for the agri_project
    Atrributes: created_at- Time of creation
                updated_at- Time of update/edit
    """
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        """Ensures BaseModel not treated as a database table"""
        abstract = True

class Project(BaseModel):
    """class that holds the agribusiness project details"""
    name = models.CharField(max_length=50, help_text="The name of agribusiness project")
    description = models.TextField(help_text="project description")
    funding_goal = models.DecimalField(max_digits=10, decimal_places=2,
            help_text="funding needed")
    current_status = models.CharField(max_length=50, default='Open',
            help_text="Open, Closed, Onhold")
    farmer_name = models.CharField(max_length=100, help_text="Your names")
    farmer_email = models.EmailField(help_text="Farmer's Email")

    def __str__(self):
        return self.name

class LoanApplication(BaseModel):
    """holds loan application details"""
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    amount_requested = models.DecimalField(max_digits=10, decimal_places=2,
            help_text="Loan amount")
    supporting_docs = models.FileField(upload_to='documents/', 
            help_text="Legal documents needed")

    def __str__(self):
        return "{} - {}".format(self.project.name, self.amount_requested)

class InvestorInterest(BaseModel):
    """holds investor details"""
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    investor_fname = models.CharField(max_length=50, help_text="Investor's first name")
    investor_lname = models.CharField(max_length=50, help_text="Investor's last name")
    investor_email = models.EmailField(help_text="investor email")
    
    def __str__(self):
        return "{} {} - {}".format(self.investor_fname, self.investor_lname, 
                self.project.name)

class Notification(BaseModel):
    """notification details to be sent to farmer"""
    recipient = models.EmailField(help_text="Farmer's email")
    message = models.TextField(help_text="notification message")

    def __str__(self):
        return "Notification to {}".format(self.recipient)
