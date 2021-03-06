from django.db import models
from datetime import date
import calendar
from django.utils import timezone
from django.conf import settings
from accounts.models import User, Employee
from projectcalendar import projectcalendar
import pytz

TIMEZONES = []
for tz in pytz.all_timezones:
    if tz[0] == 'U' or tz[0] == 'C':
        TIMEZONES.append((tz, tz))

# Create your models here.
class Project(models.Model):
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    estimated_completion_time = models.CharField(max_length=200)
    estimated_cost = models.CharField(max_length=200)
    budget = models.IntegerField(default=0)
    created_date = models.DateTimeField(auto_now_add=True)
    start_date = models.DateTimeField(default=timezone.now)
    deadline = models.DateTimeField(default=timezone.now)
    tz = models.CharField(max_length=200, choices=TIMEZONES, default=0)
    color = models.CharField(default='#191919', max_length=200, blank=True)
    complete = models.BooleanField(default=False)


    def __str__(self):
        return self.title

    @property
    def calculate_completion_percent(self):
        completed = self.feature_set.filter(complete=True).count()
        total_features = self.feature_set.count()
        percentage = 0
        if total_features > 0:
            percentage = (completed * 100) / total_features
        return percentage


    @property
    def is_past_due(self):
        if not self.complete:
            return date.today() > self.deadline.date()
        return True
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
    assigned_to = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE,
                                    related_name='feature_assignee', null=True)
    title = models.CharField(max_length=200)
    details = models.CharField(max_length=2000)
    start_date = models.DateTimeField(default=timezone.now)
    start_time = models.DateTimeField(null=True, blank=True)
    deadline = models.DateTimeField(default=timezone.now)
    end_time = models.DateTimeField(null=True, blank=True)
    start_date_time = models.DateTimeField(null=True, blank=True)
    end_date_time = models.DateTimeField(null=True, blank=True)
    color = models.CharField(default='#191919', max_length=200)
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
    start_date = models.DateTimeField(default=timezone.now)
    start_time = models.TimeField(null=True, blank=True)
    deadline = models.DateTimeField(default=timezone.now)
    end_time = models.TimeField(null=True, blank=True)
    start_date_time = models.DateTimeField(null=True, blank=True)
    end_date_time = models.DateTimeField(null=True, blank=True)
    color = models.CharField(default='#191919', max_length=200)
    estimated_completion_time = models.CharField(max_length=200, null=True, blank=True)
    cost = models.CharField(max_length=200)
    assigned_to = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE,
                                    related_name='task_assignee', null=True)
    created_date = models.DateTimeField(auto_now_add=True)
    clock_in = models.DateTimeField(null=True, blank=True)
    clock_out = models.DateTimeField(null=True, blank=True)
    complete = models.BooleanField(default=False)
    in_work = models.BooleanField(default=False)

    def __str__(self):
        return self.title

    def get_seconds_count(self):
        total = self.clock_out - self.clock_in
        return total

    @property
    def get_comment_count(self):
        return self.taskcomment_set.all().count()


class TaskComment(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    task = models.ManyToManyField(Task)
    details = models.CharField(max_length=2000)
    created_date = models.DateTimeField(auto_now_add=True)


class FeatureComment(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    feature = models.ManyToManyField(Feature)
    details = models.CharField(max_length=2000)
    created_date = models.DateTimeField(auto_now_add=True)
