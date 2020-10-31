from django.shortcuts import render, redirect
from .models import To_Do
from django.http import HttpResponseRedirect

# Create your views here.


def home_page(request):
    return render(request, 'todoapp/index.html', {})


def create_todo(request):

    whole_list = To_Do.objects.all().order_by('-time_creation')

    context = {
        'todos': whole_list
    }

    if request.method == 'GET':
        return render(request, 'todoapp/create.html', context)

    if request.method == 'POST':
        todo = request.POST.get('create_card')

        To_Do.objects.create(description=todo)

        context = {
            'todos': whole_list
        }
        return render(request, 'todoapp/create.html', context)




def todo_delete(request, todo_id):

    if request.method == 'POST':
        action = request.POST.get('submit')

        print(action)

        if action == 'Yes':
            task = To_Do.objects.get(id=todo_id)
            task.delete()
            return redirect('../create')
        else:
            return redirect('../create')