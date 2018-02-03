from django.db import models
from datetime import date
import calendar
from django.utils import timezone
from django.conf import settings
from accounts.models import User, Employee
from projectcalendar import projectcalendar

# Create your models here.
class Project(models.Model):
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    estimated_completion_time = models.CharField(max_length=200)
    estimated_cost = models.CharField(max_length=200)
    hourly_rate = models.CharField(max_length=200)
    created_date = models.DateTimeField(auto_now_add=True)
    start_date = models.DateTimeField(default=timezone.now)
    deadline = models.DateTimeField(default=timezone.now)
    complete = models.BooleanField(default=False)

    # TODO: Create status on all classes ('open', 'in-work', 'complete')

    def __str__(self):
        return self.title

    @property
    def is_past_due(self):
        return date.today() > self.deadline.date()

    @property
    def get_total_days(self):
        total_days = self.deadline.date() - self.start_date.date()
        return total_days.days


    def create_calendar(self):
        calendar = projectcalendar.ProjectCalendar(self.start_date.date(), self.deadline.date())
        calendar.create_calendar_dict()
        return calendar.create_calendar()


class Feature(models.Model):
    owner = models.ForeignKey(settings.AUTH_USER_MODEL,
                              on_delete=models.CASCADE,
                              related_name='feature_owner', default=1)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    assigned_to = models.ForeignKey(Employee, on_delete=models.CASCADE,
                                    related_name='feature_assignee', null=True)
    title = models.CharField(max_length=200)
    details = models.CharField(max_length=2000)
    estimated_completion_time = models.CharField(max_length=200)
    cost = models.CharField(max_length=200)
    created_date = models.DateTimeField(auto_now_add=True)
    complete = models.BooleanField(default=False)

    def __str__(self):
        return self.title

class Task(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    feature = models.ForeignKey(Feature, on_delete=models.CASCADE,
                                null=True, blank=True)
    title = models.CharField(max_length=200)
    details = models.CharField(max_length=2000)
    estimated_completion_time = models.CharField(max_length=200)
    cost = models.CharField(max_length=200)
    assigned_to = models.ForeignKey(Employee, on_delete=models.CASCADE,
                                    related_name='task_assignee', null=True)
    created_date = models.DateTimeField(auto_now_add=True)
    complete = models.BooleanField(default=False)

    def __str__(self):
        return self.title
