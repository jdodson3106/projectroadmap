from django.shortcuts import render, redirect, reverse
from django.urls import reverse_lazy
from django.contrib.auth import login, authenticate
from django.contrib.auth.views import login as login_form
from django.views.generic import (CreateView, ListView, TemplateView,
                                  DetailView, DeleteView, UpdateView)
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from accounts.models import User, Employee
from projects.models import Project, Feature, Task
from projects.forms import CreateProjectForm
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
