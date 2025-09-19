from django.shortcuts import render, get_object_or_404
from .models import Project, ProjectUser
from .forms import CreateProjectForm, UpdateProjectForm

# Create your views here.
def list_projects(request):
    projects = Project.objects.all()
    return render(request, 'projects.html', {'projects': projects})

def get_project(request, id):
    projet = get_object_or_404(Project, id=id)
    return render(request, 'html')

def create_project(request):
    form = CreateProjectForm()
    if request.method == "POST":
        if form.is_valid():
            form = CreateProjectForm(request.POST) # incoming data['name', 'description', 'state', 'priority']
            project = form.save(commit=False) #as the form is a model form...
            project.created_by = request.user

    else:
        form = CreateProjectForm()
        return render(request, 'html')
    
def update_project(request, id):
    form = UpdateProjectForm()
    if request.method == "POST":
        if form.is_valid():
            form = UpdateProjectForm(request.POST, instance=Project) #say to django, ill change something ...
            project_updated = form.save(commit=False)
            project_updated.updated_by = request.user
            return render (request, 'html') #add error login.

    else:
        form = UpdateProjectForm()
        return render(request, 'html')

def delete_project(request, id):
    project_to_delete = Project.objects.get(id=id)
    project_to_delete.delete()
    return render (request, 'html') #agregar mensaje de exito.