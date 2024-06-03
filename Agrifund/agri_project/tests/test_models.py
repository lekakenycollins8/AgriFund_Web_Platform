"""unittests for Agrifund models"""
from django.test import TestCase
from django.core.files.uploadedfile import SimpleUploadedFile
from ..models import Project, LoanApplication, InvestorInterest, Notification

class ProjectModelTest(TestCase):

    def setUp(self):
        self.project = Project.objects.create(
            name="Test Project",
            description="Test project description",
            funding_goal=10000.00,
            current_status="Open",
            farmer_name="John Doe",
            farmer_email="john@example.com"
        )

    def test_project_creation(self):
        self.assertIsInstance(self.project, Project)
        self.assertEqual(self.project.__str__(), self.project.name)

    def test_project_fields(self):
        self.assertEqual(self.project.name, "Test Project")
        self.assertEqual(self.project.description, "Test project description")
        self.assertEqual(self.project.funding_goal, 10000.00)
        self.assertEqual(self.project.current_status, "Open")
        self.assertEqual(self.project.farmer_name, "John Doe")
        self.assertEqual(self.project.farmer_email, "john@example.com")


class LoanApplicationModelTest(TestCase):

    def setUp(self):
        self.project = Project.objects.create(
            name="Test Project",
            description="Test project description",
            funding_goal=10000.00,
            current_status="Open",
            farmer_name="John Doe",
            farmer_email="john@example.com"
        )
        self.loan_application = LoanApplication.objects.create(
            project=self.project,
            amount_requested=5000.00,
        )

    def test_loan_application_creation(self):
        self.assertIsInstance(self.loan_application, LoanApplication)
        self.assertEqual(self.loan_application.__str__(), "{} - {}".format(self.project.name, self.loan_application.amount_requested))

    def test_loan_application_fields(self):
        self.assertEqual(self.loan_application.project, self.project)
        self.assertEqual(self.loan_application.amount_requested, 5000.00)


class InvestorInterestModelTest(TestCase):

    def setUp(self):
        self.project = Project.objects.create(
            name="Test Project",
            description="Test project description",
            funding_goal=10000.00,
            current_status="Open",
            farmer_name="John Doe",
            farmer_email="john@example.com"
        )
        self.investor_interest = InvestorInterest.objects.create(
            project=self.project,
            investor_fname="Jane",
            investor_lname="Smith",
            investor_email="jane@example.com",
            amount_offered=2000.00,
            interest_rate=10.5
        )

    def test_investor_interest_creation(self):
        self.assertIsInstance(self.investor_interest, InvestorInterest)
        self.assertEqual(self.investor_interest.__str__(), "{} {} - {}".format(self.investor_interest.investor_fname, self.investor_interest.investor_lname, self.project.name))

    def test_investor_interest_fields(self):
        self.assertEqual(self.investor_interest.project, self.project)
        self.assertEqual(self.investor_interest.investor_fname, "Jane")
        self.assertEqual(self.investor_interest.investor_lname, "Smith")
        self.assertEqual(self.investor_interest.investor_email, "jane@example.com")
        self.assertEqual(self.investor_interest.amount_offered, 2000.00)
        self.assertEqual(self.investor_interest.interest_rate, 10.5)


class NotificationModelTest(TestCase):

    def setUp(self):
        self.notification = Notification.objects.create(
            recipient="farmer@example.com",
            message="You have a new investment interest."
        )

    def test_notification_creation(self):
        self.assertIsInstance(self.notification, Notification)
        self.assertEqual(self.notification.__str__(), "Notification to {}".format(self.notification.recipient))

    def test_notification_fields(self):
        self.assertEqual(self.notification.recipient, "farmer@example.com")
        self.assertEqual(self.notification.message, "You have a new investment interest.")
