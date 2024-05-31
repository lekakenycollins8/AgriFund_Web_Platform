"""all api views for AgriFund"""

from rest_framework import viewsets
from .models import Project, LoanApplication, InvestorInterest, Notification
from .serializers import ProjectSerializer, LoanApplicationSerializer, InvestorInterestSerializer, NotificationSerializer

class ProjectViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer

class LoanApplicationViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = LoanApplication.objects.all()
    serializer_class = LoanApplicationSerializer

class InvestorInterestViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = InvestorInterest.objects.all()
    serializer_class = InvestorInterestSerializer

class NotificationViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Notification.objects.all()
    serializer_class = NotificationSerializer
