from django.urls import path
from . import views
urlpatterns = [
    path('', views.landing_page, name='landing_page'),
    path('projects/', views.project_listing, name='project_listing'),
    path('projects/<int:pk>/', views.project_details, name='project_details'),
    path('projects/create/', views.project_create, name='project_create')
]
