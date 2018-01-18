from django.urls import path
from projects import views
from projects.views import (CreateProject, ProjectDetail,)

app_name = 'projects'

urlpatterns = [
    path('project-creator', CreateProject.as_view(), name='new_project'),
    path('<int:pk>/', ProjectDetail.as_view(), name='project_view'),
    path('<int:pk>/', views.add_feature, name='add_feature'),
]
