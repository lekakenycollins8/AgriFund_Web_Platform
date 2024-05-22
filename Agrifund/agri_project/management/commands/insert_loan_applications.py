"""populates LoanApplication model with data"""

from django.core.management.base import BaseCommand
from agri_project.models import Project, LoanApplication
from decimal import Decimal
import os

class Command(BaseCommand):
    help = 'Inserts sample loan application data into the database'

    def handle(self, *args, **kwargs):
        # Assuming you have already inserted the project data, fetch the first 5 projects
        projects = Project.objects.all()[:5]

        loan_applications = [
            LoanApplication(
                project=projects[0],
                amount_requested=Decimal('10000.00'),
                supporting_docs='documents/doc1.pdf'
            ),
            LoanApplication(
                project=projects[1],
                amount_requested=Decimal('15000.00'),
                supporting_docs='documents/doc2.pdf'
            ),
            LoanApplication(
                project=projects[2],
                amount_requested=Decimal('12000.00'),
                supporting_docs='documents/doc3.pdf'
            ),
            LoanApplication(
                project=projects[3],
                amount_requested=Decimal('8000.00'),
                supporting_docs='documents/doc4.pdf'
            ),
            LoanApplication(
                project=projects[4],
                amount_requested=Decimal('20000.00'),
                supporting_docs='documents/doc5.pdf'
            ),
        ]

        LoanApplication.objects.bulk_create(loan_applications)
        self.stdout.write(self.style.SUCCESS('Successfully inserted loan application data'))

