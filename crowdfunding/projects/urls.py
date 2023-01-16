from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

urlpatterns = [
    path('projects/', views.ProjectList.as_view()),
    path('projects/<int:pk>/', views.ProjectDetail.as_view()), #we need a path that uses the project key or project id. This is the list of projects
    path('pledges/', views.PledgeList.as_view()),
    
]

   
   
urlpatterns = format_suffix_patterns(urlpatterns)