from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from .models import TodoList, Todo
from .forms import TodoListForm, TodoForm

def todo_list(request):
    lists = TodoList.objects.all()
    return render(request, "todos/todo_list.html", {"todo_lists": lists})

def todo_detail(request, id):
    todo_list = get_object_or_404(TodoList, id=id)
    todos = todo_list.todo_set.all()
    return render(request, "todos/todo_detail.html", {"todo_list": todo_list, "todos": todos})

def todo_delete(request, id):
    todo_list = get_object_or_404(TodoList, id=id)
    todo_list.delete()
    return redirect("todo-list")  # Исправленный маршрут

def todo_edit(request, id):
    todo = get_object_or_404(TodoList, id=id)
    if request.method == "POST":
        form = TodoListForm(request.POST, instance=todo)
        if form.is_valid():
            form.save()
            return redirect('todo-detail', id=todo.id)
    else:
        form = TodoListForm(instance=todo)

    return render(request, 'todos/todo_edit.html', {'form': form, 'todo': todo})

def task_delete(request, id):
    todo = get_object_or_404(Todo, id=id)
    list_id = todo.todo_list.id
    todo.delete()
    return redirect(reverse("todo-detail", args=[list_id]))  # Исправленный редирект

def task_edit(request, id):
    todo = get_object_or_404(Todo, id=id)
    if request.method == "POST":
        form = TodoForm(request.POST, instance=todo)
        if form.is_valid():
            form.save()
            return redirect(reverse("todo-detail", args=[todo.todo_list.id]))  # Исправленный редирект
    else:
        form = TodoForm(instance=todo)

    return render(request, "todos/todo_edit.html", {"form": form})
