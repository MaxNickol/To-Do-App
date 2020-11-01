from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt

from .models import To_Do
from django.http import HttpResponseRedirect

# Create your views here.
def home_page(request):
    todos = To_Do.objects.all().order_by('-id')
    return render(request, 'todoapp/index.html', {
        'todos': todos
    })


@csrf_exempt
def create_todo(request):

    print(request.POST)

    card_content = request.POST['create_card']

    print(card_content)

    To_Do.objects.create(description=card_content)

    return HttpResponseRedirect('/')



@csrf_exempt
def todo_delete(request, todo_id):
    To_Do.objects.get(id=todo_id).delete()
    print(todo_id)
    return HttpResponseRedirect('/')


def contact_view(request):
    return render(request, 'todoapp/contacts.html', {})