from django import forms
from django.forms import ModelForm
from accounts.models import User, Employee
from projects.models import Project, Feature, Task, TaskComment, FeatureComment
import pytz

TIMEZONES = []
for tz in pytz.all_timezones:
    if tz[0] == 'U' or tz[0] == 'C':
        TIMEZONES.append((tz, tz))

class CreateProjectForm(ModelForm):
    tz = forms.ChoiceField(label='Select Timezone', choices=TIMEZONES, required=True, widget=forms.Select(attrs={'class':'form-control login-field'}))

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
        project.tz = self.cleaned_data['tz']
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
        fields = ['title', 'details', 'start_date', 'start_time',
                  'deadline', 'end_time', 'assigned_to', 'color']


class TaskCommentForm(ModelForm):

    class Meta:
        model = TaskComment
        fields = ['details']

class FeatureCommentForm(ModelForm):

    class Meta:
        model = FeatureComment
        fields = ['details']
