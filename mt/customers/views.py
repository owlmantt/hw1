from django.shortcuts import render, redirect, get_object_or_404
from .models import Customer
from .forms import CustomerForm

# Создание клиента
def create_customer(request):
    if request.method == 'POST':
        form = CustomerForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('create_customer')  # Перенаправляем на эту же страницу
    else:
        form = CustomerForm()
    
    customers = Customer.objects.all()  # Получаем всех клиентов
    return render(request, 'customers/create.html', {'form': form, 'customers': customers})

# Редактирование клиента
def customer_edit(request, id):
    customer = get_object_or_404(Customer, id=id)
    if request.method == 'POST':
        form = CustomerForm(request.POST, instance=customer)
        if form.is_valid():
            form.save()
            return redirect('create_customer')  # Перенаправляем на страницу создания
    else:
        form = CustomerForm(instance=customer)
    return render(request, 'customers/create.html', {'form': form})

# Удаление клиента
def customer_delete(request, id):
    customer = get_object_or_404(Customer, id=id)
    customer.delete()
    return redirect('create_customer')

