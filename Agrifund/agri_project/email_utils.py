"""utility function for sending email to farmer"""
from django.core.mail import send_mail
from django.template.loader import render_to_string
from Agrifund.settings import EMAIL_HOST_USER

def send_investor_details_email(farmer_email, farmer_name, project_name, investor_details):
    subject = 'New Investment Interest in Your Project'
    message = render_to_string('email/investor_details.html', {
        'farmer_name': farmer_name,
        'project_name': project_name,
        'investor_fname': investor_details.investor_fname,
        'investor_lname': investor_details.investor_lname,
        'investor_email': investor_details.investor_email,
        'amount_offered': investor_details.amount_offered,
        'interest_rate': investor_details.interest_rate,
        })
    send_mail(subject, message, EMAIL_HOST_USER, [farmer_email], fail_silently=True)
