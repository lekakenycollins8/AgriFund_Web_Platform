"""unittests for views"""

from django.test import TestCase, Client
from django.urls import reverse
from django.core.files.uploadedfile import SimpleUploadedFile
from ..models import Project, LoanApplication, InvestorInterest, Notification

class AgriFundViewsTest(TestCase):

    def setUp(self):
        self.client = Client()
        self.project = Project.objects.create(
            name="Test Project",
            description="Test project description",
            funding_goal=10000.00,
            current_status="Open",
            farmer_name="John Doe",
            farmer_email="john@example.com"
        )

    def test_landing_page(self):
        response = self.client.get(reverse('landing_page'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'agri_project/landing_page.html')

    def test_project_listing(self):
        response = self.client.get(reverse('project_listing'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'agri_project/project_listings.html')
        self.assertIn(self.project, response.context['projects'])

    def test_project_details(self):
        response = self.client.get(reverse('project_details', kwargs={'pk': self.project.pk}))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'agri_project/project_details.html')
        self.assertEqual(response.context['project'], self.project)

    def test_project_create_get(self):
        response = self.client.get(reverse('project_create'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'agri_project/project_form.html')

    def test_project_create_post(self):
        response = self.client.post(reverse('project_create'), {
            'name': 'New Project',
            'description': 'New project description',
            'funding_goal': 5000.00,
            'current_status': 'Open',
            'farmer_name': 'Jane Doe',
            'farmer_email': 'jane@example.com'
        })
        self.assertEqual(response.status_code, 302)  # Redirect after successful form submission
        self.assertEqual(Project.objects.count(), 2)  # One project already exists from setUp
        new_project = Project.objects.get(name='New Project')
        self.assertEqual(new_project.description, 'New project description')

    def test_apply_loan_get(self):
        response = self.client.get(reverse('apply_loan'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'agri_project/loan_form.html')

    def test_apply_loan_post(self):
        response = self.client.post(reverse('apply_loan'), {
            'project': self.project.pk,
            'amount_requested': 5000.00,
            'supporting_docs': SimpleUploadedFile("document.pdf", b"file_content")
        })
        self.assertEqual(response.status_code, 302)  # Redirect after successful form submission
        self.assertEqual(LoanApplication.objects.count(), 1)
        loan_application = LoanApplication.objects.get(project=self.project)
        self.assertEqual(loan_application.amount_requested, 5000.00)

    def test_investor_interest_post(self):
        response = self.client.post(reverse('project_details', kwargs={'pk': self.project.pk}), {
            'investor_fname': 'Investor',
            'investor_lname': 'Name',
            'investor_email': 'investor@example.com',
            'amount_offered': 2000.00,
            'interest_rate': 10.5
        })
        self.assertEqual(response.status_code, 302)  # Redirect after successful form submission
        self.assertEqual(InvestorInterest.objects.count(), 1)
        investor_interest = InvestorInterest.objects.get(project=self.project)
        self.assertEqual(investor_interest.investor_fname, 'Investor')
        self.assertEqual(investor_interest.amount_offered, 2000.00)
