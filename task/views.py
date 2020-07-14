from django.shortcuts import render,redirect
from .models import *
from .forms import *



# Create your views here.


def todo(request):

    task=Task.objects.all()

    form = TaskForm()


    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
        
        return redirect('/')


    
    context = {'task' : task, 'form' : form }

    return render(request,'task/base.html',context)



def update_task(request,pk):

    task = Task.objects.get(id=pk)

    m_form = TaskForm(instance=task )

    if request.method == 'POST':
        m_form = TaskForm(request.POST,instance=task)
        if m_form.is_valid():
            m_form.save()
        return redirect('/')
        
        

    context = {'task' : task ,
                'form' : m_form,
                    
                    } 

    return render(request,'task/update_task.html',context)


def delete_task(request,pk):
    task = Task.objects.get(id=pk)

    if request.method == 'POST':

        task.delete()

        return redirect('/')

    context = {'task' : task}

    return render(request,'task/delete.html',context)


