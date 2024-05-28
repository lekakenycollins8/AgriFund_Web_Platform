"""Contains serializers for the AgriFund model for API's"""

from rest_framework import serializers
from .models import Project, LoanApplication, InvestorInterest

class InvestorInterestSerializer(serializers.ModelSerializer):
    """serializes investor interest instances"""
    project = serializers.CharField(source='project.name', read_only=True)
    class Meta:
        model = InvestorInterest
        fields = "__all__"

class ProjectSerializer(serializers.ModelSerializer):
    """serializes all project deatils"""
    investor_interests = InvestorInterestSerializer(many=True, read_only=True)
    class Meta:
        model = Project
        fields = "__all__"
        #fields = ['name', 'description', 'funding_goal', 'current_status',
         #       'farmer_name', 'farmer_email']

class LoanApplicationSerializer(serializers.ModelSerializer):
    """serailizes loan application details"""
    project = serializers.CharField(source='project.name', read_only=True)
    class Meta:
        model = LoanApplication
        fields = "__all__"
