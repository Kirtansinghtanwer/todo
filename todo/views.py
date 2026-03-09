from django.shortcuts import get_object_or_404, redirect, render
from django.http import HttpResponse
from .models import Task 

def addTask(request):
    task = request.POST['task']
    Task.objects.create(task = task)
    return redirect('home')

def mark_as_done(request,pk):
    task= get_object_or_404(Task,pk = pk)
    task.is_completed = True
    task.save()
    return redirect('home')
def mark_as_undone(request,pk):
    task= get_object_or_404(Task,pk = pk)
    task.is_completed = False
    task.save()
    return redirect('home')
def delet_Task(request,pk):
    task = get_object_or_404(Task,pk = pk)
    task.delete()
    return redirect('home')
def update_Task(request,pk):
    task = get_object_or_404(Task,pk=pk)
    if request.method == "POST":
        updated_task= request.POST['task']
        task.task = updated_task
        task.save()
        return redirect('home')  
    contex = {
         'task' : task,
        }
    return render(request,'edit.html',contex)