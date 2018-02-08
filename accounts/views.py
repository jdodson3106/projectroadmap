from django.shortcuts import render, redirect, reverse
from accounts.forms import RegistrationForm, NewEmployeeForm
from django.urls import reverse_lazy
from django.contrib.auth import login, authenticate
from django.contrib.auth.views import login as login_form
from django.views.generic import (CreateView, ListView, TemplateView,
                                  DetailView, DeleteView, UpdateView)
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from accounts.models import User, Employee
from projects.models import Project, Feature
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.
def index(request):
    return render(request, 'accounts/index.html')

def myProfile(request):
    if request.user.admin:
        return redirect('accounts:admin_home', pk=request.user.pk)
    elif not request.user.admin:
        return redirect('accounts:user_profile', pk=request.user.pk)
    else:
        return render(request, 'accounts/index.html')


class CreateUserView(CreateView):
    model = User
    form_class = RegistrationForm
    template_name = 'accounts/register.html'

    def get_success_url(self):
        user = authenticate(email=self.request.POST['email'],
                            password=self.request.POST['password1'])
        if user.is_active:
            login(self.request, user)
            return reverse_lazy('accounts:my_profile')
        else:
            return reverse_lazy('accounts:register')


class CreateEmployee(CreateView):
    model = Employee
    form_class = NewEmployeeForm
    template_name = 'accounts/new_employee.html'

    def form_valid(self, form):
        form.instance.boss = self.request.user
        return super(CreateEmployee, self).form_valid(form)

    def get_success_url(self):
        return reverse_lazy('accounts:my_profile')



class AdminProfileView(LoginRequiredMixin, DetailView):
    model = User
    template_name = 'accounts/admin_home.html'


    def get_context_data(self, **kwargs):
        context = super(AdminProfileView, self).get_context_data(**kwargs)
        employees = Employee.objects.filter(boss=self.get_object())
        context['employees'] = employees
        projects = Project.objects.filter(owner=self.get_object()).order_by('-created_date')
        context['projects'] = projects
        return context

class UserProfileView(DetailView):
    model = User
    template_name = 'accounts/user_profile.html'
