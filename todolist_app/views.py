from django.shortcuts import redirect, render
from .models import TaskList
from .forms import TaskForm
from django.contrib import messages
from django.core.paginator import Paginator

# Create your views here.


def index(request):
    return render(request, 'index.html')


def todolist(request):
    if request.method == 'POST':
        form = TaskForm(request.POST or None)
        if form.is_valid():
            form.save()
            messages.success(request, ("New Task Added"))
        return redirect('todolist') 
    else:
        all_tasks = TaskList.objects.all().order_by('id')
        paginator=Paginator(all_tasks,4)
        page=request.GET.get('pg')
        all_tasks = paginator.get_page(page)
        context = {
            'all_tasks': all_tasks,
        }
        return render(request, 'todolist.html', context)


def contact(request):
    return render(request, 'contact.html')


def about(request):
    return render(request, 'about.html')

def delete_task(request, task_id):
    task=TaskList.objects.get(pk=task_id)
    task.delete()
    return redirect('todolist')

def edit_task(request, task_id):  
    if request.method == 'POST':
        task=TaskList.objects.get(pk=task_id)
        form=TaskForm(request.POST or None,instance=task)
        if form.is_valid():
            form.save()
            messages.success(request, ("Task Edited"))
        return redirect('todolist')
    else:
        task_obj = TaskList.objects.get(pk=task_id)
        context = {
            'task_obj': task_obj,
        }
        return render(request, 'edit.html', context)  

def complete_task(request, task_id):
    task = TaskList.objects.get(pk=task_id)
    task.done=True   
    task.save() 
    return redirect('todolist')

def pending_task(request, task_id):
    task = TaskList.objects.get(pk=task_id)
    task.done=False 
    task.save()    
    return redirect('todolist') 

