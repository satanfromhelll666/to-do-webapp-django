from django.shortcuts import render,redirect
from .models import *
from .forms import *
from django.http import JsonResponse

from rest_framework.decorators import api_view
from rest_framework.response import Response 

from .serializer import TaskSerializer




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


@api_view(['GET'])

def apiOverview(request):

    api_urls = {
    'List':'/task-list/',
    'Detail View':'/task-detail/<str:pk>/',
    'Create':'/task-create/',
    'Update':'/task-update/<str:pk>/',
    'Delete':'/task-delete/<str:pk>/',
    }

    return Response(api_urls)


@api_view(['GET'])

def taskList(request):

    tasks = Task.objects.all()

    serializer = TaskSerializer(tasks,many=True)

    return Response(serializer.data)



@api_view(['GET'])

def taskDetail(request,pk):

    tasks = Task.objects.get(id=pk)

    serializer = TaskSerializer(tasks,many=False)

    return Response(serializer.data)


@api_view(['POST'])

def taskCreate(request):


    serializer = TaskSerializer(data= request.data)

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)


@api_view(['POST'])

def taskUpdate(request,pk):

    tasks = Task.objects.get(id=pk)

    serializer = TaskSerializer(instance=tasks , data= request.data)

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)


@api_view(['DELETE'])

def taskDelete(request,pk):

    tasks = Task.objects.get(id=pk)

    tasks.delete()

    return Response('successfully delete')
