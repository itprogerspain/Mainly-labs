from django import forms
from .models import Project



class CreateProjectForm(forms.ModelForm):
    class Meta:
        Model = Project
        field = ['name', 'description', 'state', 'priority']


class UpdateProjectForm(forms.ModelForm):
    class Meta:
        Model = Project
        field = ['name',  'description', 'state', 'priority']

