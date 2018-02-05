from django.shortcuts import render, redirect, reverse
from django.urls import reverse_lazy
from django.http import JsonResponse
from django.utils.safestring import mark_safe
from django.shortcuts import get_list_or_404, get_object_or_404
from django.contrib.auth import login, authenticate
from django.contrib.auth.views import login as login_form
from django.views.generic import (CreateView, ListView, TemplateView,
                                  DetailView, DeleteView, UpdateView)
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from accounts.models import User, Employee
from projects.models import Project, Feature, Task
from projects.forms import CreateProjectForm, FeatureCreationForm, TaskCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from contextualdata.context_manage import ContextManager


class CreateProject(CreateView):
    models = Project
    form_class = CreateProjectForm
    template_name = 'projects/create_project.html'

    def get_success_url(self):
        return reverse_lazy('projects:project_view', kwargs={'pk' : self.object.pk})

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super(CreateProject, self).form_valid(form)


class ProjectDetail(DetailView):
    model = Project
    template_name = 'projects/project_view.html'

    def get_context_data(self, **kwargs):
        context = super(ProjectDetail, self).get_context_data(**kwargs)
        new_feature_form = FeatureCreationForm()
        context['new_feature_form'] = new_feature_form
        features = Feature.objects.filter(project=self.get_object())
        context['features'] = features
        employees = Employee.objects.filter(boss=self.object.owner)
        context['employees'] = employees
        calendar = self.object.create_calendar()
        context['test_cal'] = calendar
        context['calendar'] = mark_safe(calendar)
        return context

class ProjectDelete(DeleteView):
    model = Project
    template_name = 'projects/project_delete.html'
    success_url = reverse_lazy('accounts:my_profile')

def add_feature(request, pk):
    form = FeatureCreationForm(request.POST or None)
    project = get_object_or_404(Project, pk=pk)

    if form.is_valid():
        print('form is valid')
        feature = Feature()
        feature.owner = request.user
        feature.project = project
        feature.title = form.cleaned_data.get('title')
        feature.details = form.cleaned_data.get('details')
        feature.start_date = form.cleaned_data.get('start_date')
        feature.deadline = form.cleaned_data.get('deadline')
        feature.assigned_to = form.cleaned_data.get('assigned_to')
        feature.color = form.cleaned_data.get('color')
        feature.save()
        return redirect('projects:project_view', pk=pk)
    else:
        print('from invalid')
    args = {'form':form, 'project':project}
    return redirect('accounts:admin_home', pk=project.owner.pk)

class FeatureView(DetailView):
    model = Feature
    template_name = 'projects/feature_detail.html'

    def get_context_data(self, **kwargs):
        context = super(FeatureView, self).get_context_data(**kwargs)
        new_task_form = FeatureCreationForm()
        context['new_task_form'] = new_task_form
        tasks = Task.objects.filter(feature=self.get_object())
        context['tasks'] = tasks
        employees = Employee.objects.filter(boss=self.object.project.owner)
        context['employees'] = employees
        return context

class DeleteFeature(DeleteView):
    model = Feature
    template_name = 'projects/delete_feature.html'

    def get_success_url(self):
        project = self.object.project
        return reverse_lazy('projects:project_view', kwargs={'pk': project.pk})

def mark_feature_complete(request, pk):
    feature = get_object_or_404(Feature, pk=pk)
    feature.complete = True
    feature.save()
    return redirect('projects:feature_view', pk=pk)

# TODO: Add slug field to project to create specific call variables between
#       feature and project calls.
# TODO: Create Breadcrumbs to track where you are in the project
def add_task_to_feature(request, pk):
    form = TaskCreationForm(request.POST or None)
    feature = get_object_or_404(Feature, pk=pk)

    if form.is_valid():
        task = Task()
        task.feature = feature
        task.project = feature.project
        task.title = form.cleaned_data.get('title')
        task.details = form.cleaned_data.get('details')
        task.estimated_completion_time = form.cleaned_data.get('estimated_completion_time')
        task.assigned_to = form.cleaned_data.get('assigned_to')
        task.save()
        return redirect('projects:feature_view', pk=pk)
    args = {'form':form, 'feature':feature}
    return redirect('accounts:admin_home', pk=feature.project)

class TaskDetail(DetailView):
    model = Task
    template_name = 'projects/task_view.html'

class DeleteTask(DeleteView):
    model = Task
    template_name = 'projects/delete_task.html'

    def get_success_url(self):
        feature = self.object.feature
        return reverse_lazy( 'projects:feature_view', kwargs={'pk': feature.pk})


def get_feature_object(request):
    feature = get_object_or_404(Feature, pk=pk)
    data = {
        "pk": feature.pk
    }
    return JsonResponse(data)
