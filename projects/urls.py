from django.urls import path
from projects import views
from projects.views import (CreateProject, ProjectDetail, ProjectDelete,
                            FeatureView)

app_name = 'projects'

urlpatterns = [
    path('project-creator', CreateProject.as_view(), name='new_project'),
    path('<int:pk>/', ProjectDetail.as_view(), name='project_view'),
    path('project/<int:pk>/add-feature', views.add_feature, name='add_feature'),
    path('<int:pk>/delete/', ProjectDelete.as_view(), name='delete_project'),
    path('feature/<int:pk>', FeatureView.as_view(), name='feature_veiw'), # TODO: Add slug to project model
]
