from django.contrib import admin
from django.urls import path, include
from django.shortcuts import render
from customers.models import Customer
from tables.models import Table
from reservations.models import Reservation

# Главная страница с выводом данных
def home(request):
    customers = Customer.objects.all()
    tables = Table.objects.all()
    reservations = Reservation.objects.all()
    
    return render(request, 'home.html', {
        'customers': customers,
        'tables': tables,
        'reservations': reservations
    })

urlpatterns = [
    path('admin/', admin.site.urls),
    path('customers/', include('customers.urls')),
    path('tables/', include('tables.urls')),
    path('reservations/', include('reservations.urls')),

    # Главная страница
    path('', home, name='home'),
]
