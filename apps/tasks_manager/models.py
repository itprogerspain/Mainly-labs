from django.db import models
from apps.accounts.models import CustomUser
from apps.projects_manager.models import Project

# Create your models here.
class Task(models.Model):

    STATE_CHOICES = [
        ('complete', 'complete'),
        ('incomplete', 'incomplete'),
    ]

    name = models.CharField(max_length=100)
    state = models.CharField(max_length=20, choices=STATE_CHOICES,default='incomplete')
    created_by = models.ForeignKey(CustomUser, on_delete=models.SET_NULL, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True) # create a datetime field each time a row is created
    updated_at = models.DateTimeField(auto_now=True) # update this field wich is a datetime field each time is updated.
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)


    def __str__(self):
        return f"Task: {self.name}"
