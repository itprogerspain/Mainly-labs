from django.shortcuts import get_object_or_404, render, redirect
from .models import Task
from projects_manager.models import Project
from .forms import CreateTaskForm, UpdateTaskForm


# Create your views here.
def list_tasks(request, project_id):
    tasks = Task.objects.filter(project_id=project_id)
    return render(request, "tasks.html", {'tasks': tasks})  #revisar.

def create_task(request,project_id):
    project = get_object_or_404(Project.objects.get(id=project_id))

    if request.method == "POST":
        form = CreateTaskForm(request.POST)
        if form.is_valid():
            task_to_add = form.save(commit=False)
            task_to_add.project = project
            task_to_add.user = request.user
            task_to_add.save()
            return redirect(request, "tasks.html", {'tasks': list_tasks})
        else:
            form = CreateTaskForm(request, "CreateTaskForm", {"form": form})
            return redirect()
    form = CreateTaskForm()
    return render(request, )
    

def update_task(request,project_id):
    project = get_object_or_404(Project.objects.get(id=project_id))

    if request.method == "POST":
        form = UpdateTaskForm(request.POST, instance=Task)
        if form.is_valid():
            task = form.save(commit=False)
            task.project = project
            task.user = request.user
            task.save()
            return redirect(request, "tasks.html", {'tasks': list_tasks})
        else:
            form = UpdateTaskForm()
            return redirect(request, "UpdateTaskForm.html", {"form": form})
    return render(request, "UpdateTaskForm.html", {"form": form})
                  
def delete_task(request, project_id):
    task = get_object_or_404(Task, project_id=project_id)
    task.delete()
    return redirect("tasks")