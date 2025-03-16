from django.shortcuts import render, redirect, get_object_or_404
from .models import Table
from .forms import TableForm


# Создание стола
def create_table(request):
    if request.method == 'POST':
        form = TableForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('create_table')  # Перенаправляем на эту же страницу
    else:
        form = TableForm()
    
    tables = Table.objects.all()  # Получаем все столы
    return render(request, 'tables/create.html', {'form': form, 'tables': tables})

# Редактирование стола
def table_edit(request, id):
    table = get_object_or_404(Table, id=id)
    if request.method == 'POST':
        form = TableForm(request.POST, instance=table)
        if form.is_valid():
            form.save()
            return redirect('create_table')  # Перенаправляем на страницу создания
    else:
        form = TableForm(instance=table)
    return render(request, 'tables/create.html', {'form': form})

# Удаление стола
def table_delete(request, id):
    table = get_object_or_404(Table, id=id)
    table.delete()
    return redirect('create_table')


# views.py

# views.py

from django.shortcuts import render, redirect
from .forms import AdminLoginForm

def admin_login(request):
    if request.method == 'POST':
        form = AdminLoginForm(request.POST)
        if form.is_valid():
            # Проверяем пароль
            if form.cleaned_data['password'] == 'your_admin_password':  # Замените на свой пароль
                request.session['is_admin'] = True  # Устанавливаем флаг администратора
                return redirect('home')  # Перенаправляем на главную страницу
            else:
                form.add_error('password', 'Неверный пароль')
    else:
        form = AdminLoginForm()

    return render(request, 'admin_login.html', {'form': form})

# tables/views.py
from django.shortcuts import render

def home(request):
    return render(request, 'home.html')  # или любой другой шаблон
