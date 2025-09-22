from django import forms
from .models import Task



class CreateTaskForm(forms.ModelForm):
    class Meta:
        model = Task
        field = ['name', 'state']

class UpdateTaskForm(forms.ModelForm):
    class Meta:
        model = Task
        field = ['name']

from django.urls import path
from . import views