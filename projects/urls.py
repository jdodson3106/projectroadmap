from django.urls import path
from projects import views
from projects.views import (CreateProject, ProjectDetail, ProjectDelete,
                            FeatureView, DeleteFeature, TaskDetail, DeleteTask)

app_name = 'projects'

urlpatterns = [
    path('project-creator', CreateProject.as_view(), name='new_project'),
    path('<int:pk>/', ProjectDetail.as_view(), name='project_view'),
    path('feature/get_json_pk', views.get_feature_object, name='feature_object_json'),
    path('project/<int:pk>/add-feature', views.add_feature, name='add_feature'),
    path('<int:pk>/delete/', ProjectDelete.as_view(), name='delete_project'),
    path('feature/<int:pk>', FeatureView.as_view(), name='feature_view'), # TODO: Add slug to project model
    path('feature/<int:pk>/edit', views.update_feature, name='update_feature'),
    path('feature/<int:pk>/delete', DeleteFeature.as_view(), name='delete_feature'),
    path('feature/<int:pk>/marked_complete', views.mark_feature_complete, name='marked_complete'),
    path('feature/<int:pk>/marked_incomplete', views.mark_feature_incomplete, name='marked_incomplete'),
    path('feature/<int:pk>/comment', views.new_feature_comment, name='new_feature_comment'),
    path('task/<int:pk>/add-task', views.add_task_to_feature, name='add_task'),
    path('task/<int:pk>', TaskDetail.as_view(), name='task_view'),
    path('task/<int:pk>/delete', DeleteTask.as_view(), name='delete_task'),
    path('task/<int:pk>/edit', views.update_task, name='update_task'),
    path('task/<int:pk>/comment', views.new_task_comment, name='new_task_comment'),
    path('task/<int:pk>/marked_complete', views.mark_task_complete, name='task_marked_complete'),
    path('task/<int:pk>/marked_incomplete', views.mark_task_incomplete, name='task_marked_incomplete'),
    path('task/<int:pk>/clock-in', views.task_clock_in, name='clock_in'),
    path('task/<int:pk>/clock-out', views.task_clock_out, name='clock_out'),
]
