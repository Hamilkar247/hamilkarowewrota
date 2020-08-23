from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from .models import TodoItem
from .models import List
from .forms import ListForm
from django.contrib import messages


# Create your views here.

# def witam(request):
#    return HttpResponse("Witam")

def todoView(request):
    all_todo_items = TodoItem.objets.all()
    return render(request, 'todos/todo.html',
                  {'all_items': all_todo_items})


def addTodo(request):
    new_item = TodoItem(content=request.POST['content'])
    new_item.save()
    return HttpResponseRedirect('todos')


def deleteTodo(request, todo_id):
    item_to_delete = TodoItem.objects.get(id=todo_id)
    item_to_delete.delete()
    return HttpResponseRedirect('/todos/')


def home(request):
    if request.method == 'POST':
        form = ListForm(request.POST)

        if form.is_valid():
            form.save()
            all_items = List.objects.all
            messages.success(request, 'Item Has Been Added To List!')
            return render(request, 'todos/home.html', {'all_items': all_items})
        return HttpResponse('cos nie pykło')
    else:
        all_items = List.objects.all
        return render(request, 'todos/home.html', {'all_items': all_items})
