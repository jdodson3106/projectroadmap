from django.db import models
from django.conf import settings
from accounts.models import User, Employee

# Create your models here.
class Project(models.Model):
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    estimated_completion_time = models.CharField(max_length=200)
    estimated_cost = models.CharField(max_length=200)
    hourly_rate = models.CharField(max_length=200)
    # TODO: Create a create_at field to track project creation
    # TODO: Create status on all classes ('open', 'in-work', 'complete')
    # TODO: Create completed_at field to track projects completion
    def __str__(self):
        return self.title


class Feature(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    details = models.CharField(max_length=2000)
    estimated_completion_time = models.CharField(max_length=200)
    cost = models.CharField(max_length=200)

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

    def __str__(self):
        return self.title
