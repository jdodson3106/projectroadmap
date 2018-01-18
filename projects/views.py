from django.shortcuts import render, redirect, reverse
from django.urls import reverse_lazy
from django.contrib.auth import login, authenticate
from django.contrib.auth.views import login as login_form
from django.views.generic import (CreateView, ListView, TemplateView,
                                  DetailView, DeleteView, UpdateView)
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from accounts.models import User, Employee
from projects.models import Project, Feature, Task
from projects.forms import CreateProjectForm, FeatureCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.
class CreateProject(CreateView):
    models = Project
    form_class = CreateProjectForm
    template_name = 'projects/create_project.html'

    def get_success_url(self):
        return reverse_lazy('accounts:my_profile')

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super(CreateProject, self).form_valid(form)


class ProjectDetail(DetailView):
    model = Project
    template_name = 'projects/project_view.html'

def add_feature(request, pk):
    form = FeatureCreationForm(request.POST or None)
    project = get_list_or_404(Project, pk=pk)

    if form.is_valid():
        feature = Feature()
        feature.owner = request.user
        feature.title = form.cleaned_data.get('title')
        feature.details = form.cleaned_data.get('details')
        feature.estimated_completion_time = form.cleaned_data.get('estimated_completion_time')
        feature.assigned_to = form.cleaned_data.get('assigned_to')
        feature.save()
        project.features.add(feature)
        return redirect('projects:project_view', pk=pk)
    return redirect('accounts:my_profile')
