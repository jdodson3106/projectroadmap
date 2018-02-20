from django.shortcuts import render, redirect, reverse
from django.urls import reverse_lazy
from django.http import JsonResponse
from django.template.loader import render_to_string
from django.utils.safestring import mark_safe
from django.shortcuts import get_list_or_404, get_object_or_404
from django.contrib.auth import login, authenticate
from django.contrib.auth.views import login as login_form
from django.views.generic import (CreateView, ListView, TemplateView,
                                  DetailView, DeleteView, UpdateView)
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from accounts.models import User, Employee
from projects.models import Project, Feature, Task, FeatureComment, TaskComment
from projects.forms import (CreateProjectForm, FeatureCreationForm,
                            TaskCreationForm, FeatureCommentForm, TaskCommentForm)
from django.contrib.auth.mixins import LoginRequiredMixin
from contextualdata.context_manage import ContextManager
import datetime
from datetime import date


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
        project = self.object
        new_feature_form = FeatureCreationForm()
        context['new_feature_form'] = new_feature_form
        features = Feature.objects.filter(project=self.get_object())
        context['features'] = features
        employees = Employee.objects.filter(boss=self.object.owner)
        context['employees'] = employees
        return context



class ProjectDelete(DeleteView):
    model = Project
    template_name = 'projects/project_delete.html'
    success_url = reverse_lazy('accounts:my_profile')

def add_feature(request, pk):
    print(pk)
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
        for error in form.errors:
            print(error)
        print('from invalid')
    args = {'form':form, 'project':project}
    return redirect('accounts:admin_home', pk=project.owner.pk)


def update_feature(request, pk):
    data = dict()
    feature = get_object_or_404(Feature, pk=pk)
    form = FeatureCreationForm(request.POST, instance=feature)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            data['form_is_valid'] = True
        else:
            form = FeatureCreationForm(instance=feature)
            data['form_is_valid'] = False
    template_name = 'projects/partial_edit_feature.html'
    context = {'form': form}
    data['html_form'] = render_to_string(template_name, context, request=request)
    data['working'] = True
    return JsonResponse(data)

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
        notes = FeatureComment.objects.filter(feature=self.get_object())
        context['notes'] = notes
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

def mark_feature_incomplete(request, pk):
    feature = get_object_or_404(Feature, pk=pk)
    feature.complete = False
    feature.save()
    return redirect('projects:feature_view', pk=pk)


def new_feature_comment(request, pk):
    feature = get_object_or_404(Feature, pk=pk)
    form = FeatureCommentForm(request.POST or None)

    if form.is_valid():
        print('valid')
        comment = FeatureComment()
        comment.author = request.user
        comment.details = form.cleaned_data.get('details')
        comment.save()
        comment.feature.add(feature)
        return redirect('projects:feature_view', pk=pk)
    print("not valid")
    args = {'alert':'Comment Not Added', 'form':form} # TODO: figure out how to send args with redirect
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
        task.start_date = form.cleaned_data.get('start_date')
        task.start_time = form.cleaned_data.get('start_time')
        task.start_date_time = datetime.datetime.combine(task.start_date, task.start_time)
        task.deadline = form.cleaned_data.get('deadline')
        task.end_time = form.cleaned_data.get('end_time')
        task.end_date_time = datetime.datetime.combine(task.deadline, task.end_time)
        task.assigned_to = form.cleaned_data.get('assigned_to')
        task.color = form.cleaned_data.get('color')
        task.save()
        print("valid")
        return redirect('projects:feature_view', pk=pk)
    args = {'form':form, 'feature':feature}
    for error in form.errors:
        print(error)
    return redirect('projects:feature_view', pk=pk)

def update_task(request, pk):
    data = dict()
    task = get_object_or_404(Task, pk=pk)
    form = TaskCreationForm(request.POST, instance=task)
    if request.method == 'POST':
        if form.is_valid():
            task.start_date = form.cleaned_data.get('start_date')
            task.start_time = form.cleaned_data.get('start_time')
            task.start_date_time = datetime.datetime.combine(task.start_date, task.start_time)
            task.deadline = form.cleaned_data.get('deadline')
            task.end_time = form.cleaned_data.get('end_time')
            task.end_date_time = datetime.datetime.combine(task.deadline, task.end_time)
            form.save()
            data['form_is_valid'] = True
        else:
            form = TaskCreationForm(instance=task)
            data['form_is_valid'] = False
    template_name = 'projects/partial_edit_task.html'
    context = {'form': form}
    data['html_form'] = render_to_string(template_name, context, request=request)
    data['working'] = True
    return JsonResponse(data)

class TaskDetail(DetailView):
    model = Task
    template_name = 'projects/task_view.html'

    def get_context_data(self, **kwargs):
        context = super(TaskDetail, self).get_context_data(**kwargs)
        notes = TaskComment.objects.filter(task=self.get_object())
        context['notes'] = notes
        return context


class DeleteTask(DeleteView):
    model = Task
    template_name = 'projects/delete_task.html'

    def get_success_url(self):
        feature = self.object.feature
        return reverse_lazy( 'projects:feature_view', kwargs={'pk': feature.pk})

def mark_task_complete(request, pk):
    task = get_object_or_404(Task, pk=pk)
    task.complete = True
    task.save()
    return redirect('projects:task_view', pk=pk)

def mark_task_incomplete(request, pk):
    task = get_object_or_404(Task, pk=pk)
    task.complete = False
    task.save()
    return redirect('projects:task_view', pk=pk)

def new_task_comment(request, pk):
    task = get_object_or_404(Task, pk=pk)
    form = TaskCommentForm(request.POST or None)
    if form.is_valid():
        print("valid")
        comment = TaskComment()
        comment.author = request.user
        comment.details = form.cleaned_data.get('details')
        comment.save()
        comment.task.add(task)
        return redirect('projects:task_view', pk=pk)
    for errors in form.errors:
        print(errors)
    return redirect('projects:task_view', pk=pk)


def get_feature_object(request):
    feature = get_object_or_404(Feature, pk=pk)
    data = {
        "pk": feature.pk
    }
    return JsonResponse(data)


"""
    Time handler for clocking in and out of tasks. Needs to send a JsonResponse
    to the front end so jQuery can increment time. Only start and stop are managed
    with the db and django. jQuery will handle the rest on the front end.
"""
# TODO: Add handler for in request is not an ajax request on clock in and out
def task_clock_in(request, pk):
    if request.is_ajax():
        data = dict()
        task = get_object_or_404(Task, pk=pk)
        task.clock_in = datetime.datetime.now().time()
        task.in_work = True
        task.save()
        # print(task.clock_in)
        data['clock_in'] = task.clock_in
        data['in_work'] = task.in_work
        return JsonResponse(data)

def task_clock_out(request, pk):
    if request.is_ajax():
        data = dict()
        task = get_object_or_404(Task, pk=pk)
        task.clock_out = datetime.datetime.now().time()
        task.in_work = False
        task.save()
        # print(datetime.datetime.combine(date.min, task.clock_out) - datetime.datetime.combine(date.min, task.clock_in))
        data['clock_out'] = task.clock_out
        data['in_work'] = task.in_work
        return JsonResponse(data)
