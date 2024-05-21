
from django.core.management.base import BaseCommand
from agri_project.models import Project
from decimal import Decimal

class Command(BaseCommand):
    help = 'Inserts sample project data into the database'

    def handle(self, *args, **kwargs):
        projects = [
            Project(
                name="Organic Vegetable Farming",
                description="A project focused on cultivating organic vegetables using sustainable farming practices to provide healthy food options and promote environmental sustainability.",
                funding_goal=Decimal('15000.00'),
                current_status="Open",
                farmer_name="John Doe",
                farmer_email="johndoe@example.com"
            ),
            Project(
                name="Dairy Farm Expansion",
                description="Expanding an existing dairy farm to increase milk production and supply high-quality dairy products to the local community.",
                funding_goal=Decimal('25000.00'),
                current_status="Open",
                farmer_name="Jane Smith",
                farmer_email="janesmith@example.com"
            ),
            Project(
                name="Solar-Powered Irrigation System",
                description="Implementing a solar-powered irrigation system to reduce energy costs and improve water efficiency for a large-scale farm.",
                funding_goal=Decimal('20000.00'),
                current_status="Open",
                farmer_name="Robert Brown",
                farmer_email="robertbrown@example.com"
            ),
            Project(
                name="Bee Conservation and Honey Production",
                description="Establishing a bee farm to promote pollination and produce high-quality honey while supporting bee conservation efforts.",
                funding_goal=Decimal('10000.00'),
                current_status="Open",
                farmer_name="Emily Davis",
                farmer_email="emilydavis@example.com"
            ),
            Project(
                name="Aquaponics Fish Farming",
                description="Developing an aquaponics system that combines fish farming and hydroponic vegetable cultivation to create a sustainable food production system.",
                funding_goal=Decimal('30000.00'),
                current_status="Open",
                farmer_name="Michael Wilson",
                farmer_email="michaelwilson@example.com"
            ),
            Project(
                name="High-Yield Wheat Production",
                description="Enhancing wheat production using advanced agricultural techniques to increase yield and support local food supply.",
                funding_goal=Decimal('18000.00'),
                current_status="Open",
                farmer_name="Sarah Johnson",
                farmer_email="sarahjohnson@example.com"
            ),
            Project(
                name="Urban Rooftop Farming",
                description="Creating rooftop gardens in urban areas to grow fresh vegetables and herbs, reducing food miles and promoting urban agriculture.",
                funding_goal=Decimal('12000.00'),
                current_status="Open",
                farmer_name="William Taylor",
                farmer_email="williamtaylor@example.com"
            ),
            Project(
                name="Apple Orchard Modernization",
                description="Modernizing an apple orchard with new equipment and techniques to improve fruit quality and increase production efficiency.",
                funding_goal=Decimal('22000.00'),
                current_status="Open",
                farmer_name="Jessica Moore",
                farmer_email="jessicamoore@example.com"
            ),
            Project(
                name="Free-Range Poultry Farming",
                description="Establishing a free-range poultry farm to produce organic eggs and meat while ensuring animal welfare and environmental sustainability.",
                funding_goal=Decimal('16000.00'),
                current_status="Open",
                farmer_name="Thomas Anderson",
                farmer_email="thomasanderson@example.com"
            ),
            Project(
                name="Vineyard Development for Organic Wine",
                description="Developing a vineyard to produce organic wine, focusing on sustainable viticulture practices and high-quality grape production.",
                funding_goal=Decimal('28000.00'),
                current_status="Open",
                farmer_name="Karen Martinez",
                farmer_email="karenmartinez@example.com"
            ),
        ]

        Project.objects.bulk_create(projects)
        self.stdout.write(self.style.SUCCESS('Successfully inserted project data'))

