from django.shortcuts import render, redirect
from .models import Todo
from django.contrib import messages
# Create your views here.

def todo(request):
    if request.method == 'POST':
        todo = request.POST.get('todo')
        Todo.objects.create(todo = todo)
        messages.add_message(request, messages.INFO, 'Todo Created' )
        context = {'todos':Todo.objects.all()}
        return redirect('/')
    return render(request, 'todo.html', context)