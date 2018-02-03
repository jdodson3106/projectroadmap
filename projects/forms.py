from django.forms import ModelForm
from accounts.models import User, Employee
from projects.models import Project, Feature, Task


class CreateProjectForm(ModelForm):

    class Meta:
        model = Project
        fields = ['title','start_date',
                  'deadline', 'hourly_rate']

    def save(self):
        project = super(CreateProjectForm, self).save(commit=False)
        project.title = self.cleaned_data['title']
        project.start_date = self.cleaned_data['start_date']
        project.deadline = self.cleaned_data['deadline']
        project.hourly_rate = self.cleaned_data['hourly_rate']

        project.save()
        return project

class FeatureCreationForm(ModelForm):

    class Meta:
        model = Feature
        fields = ['title', 'details', 'estimated_completion_time', 'assigned_to']


class TaskCreationForm(ModelForm):

    class Meta:
        model = Task
        fields = ['title', 'details', 'estimated_completion_time', 'assigned_to']
