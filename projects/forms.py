from django.forms import ModelForm
from accounts.models import User, Employee
from projects.models import Project, Feature, Task


class CreateProjectForm(ModelForm):

    class Meta:
        model = Project
        fields = ['title','estimated_completion_time',
                  'estimated_cost', 'hourly_rate']

    def save(self):
        project = super(CreateProjectForm, self).save(commit=False)
        project.title = self.cleaned_data['title']
        project.estimated_completion_time = self.cleaned_data['estimated_completion_time']
        project.estimated_cost = self.cleaned_data['estimated_cost']
        project.hourly_rate = self.cleaned_data['hourly_rate']

        project.save()
        return project

class FeatureCreationForm(ModelForm):

    class Meta:
        model = Feature
        fields = ['title', 'details', 'estimated_completion_time', 'assigned_to' ]


class TaskCreationForm(ModelForm):

    class Meta:
        model = Task
        fields = ['title', 'details', 'estimated_completion_time', 'assigned_to']
