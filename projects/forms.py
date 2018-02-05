from django.forms import ModelForm
from accounts.models import User, Employee
from projects.models import Project, Feature, Task


class CreateProjectForm(ModelForm):

    class Meta:
        model = Project
        fields = ['title','start_date',
                  'deadline', 'budget', 'color']

    def save(self):
        project = super(CreateProjectForm, self).save(commit=False)
        project.title = self.cleaned_data['title']
        project.start_date = self.cleaned_data['start_date']
        project.deadline = self.cleaned_data['deadline']
        project.budget = self.cleaned_data['budget']
        project.color = self.cleaned_data['color']

        project.save()
        return project

class FeatureCreationForm(ModelForm):

    class Meta:
        model = Feature
        fields = ['title', 'details', 'start_date',
                  'deadline', 'assigned_to', 'color']


class TaskCreationForm(ModelForm):

    class Meta:
        model = Task
        fields = ['title', 'details', 'start_date',
                  'deadline', 'assigned_to', 'color']
