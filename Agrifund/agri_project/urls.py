from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views, api_views

# router automatically genrates url patterns for ViewSets

router = DefaultRouter()
router.register(r'projects', api_views.ProjectViewSet)
router.register(r'loans', api_views.LoanApplicationViewSet)
router.register(r'investors', api_views.InvestorInterestViewSet)
router.register(r'notifications', api_views.NotificationViewSet)

urlpatterns = [
    path('', views.landing_page, name='landing_page'),
    path('api/', include((router.urls, 'api'))),
    path('projects/', views.project_listing, name='project_listing'),
    path('projects/<int:pk>/', views.project_details, name='project_details'),
    path('projects/create/', views.project_create, name='project_create'),
    path('loans/', views.apply_loan, name='apply_loan'),
]
