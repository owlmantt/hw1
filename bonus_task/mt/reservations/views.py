from django.shortcuts import render, redirect, get_object_or_404
from .models import Reservation
from .forms import ReservationForm

# Создание бронирования
def create_reservation(request):
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('create_reservation')  # Перенаправляем на эту же страницу
    else:
        form = ReservationForm()
    
    reservations = Reservation.objects.all()  # Получаем все бронирования
    return render(request, 'reservations/create.html', {'form': form, 'reservations': reservations})

# Редактирование бронирования
def reservation_edit(request, id):
    reservation = get_object_or_404(Reservation, id=id)
    if request.method == 'POST':
        form = ReservationForm(request.POST, instance=reservation)
        if form.is_valid():
            form.save()
            return redirect('create_reservation')  # Перенаправляем на страницу создания
    else:
        form = ReservationForm(instance=reservation)
    return render(request, 'reservations/create.html', {'form': form})

# Удаление бронирования
def reservation_delete(request, id):
    reservation = get_object_or_404(Reservation, id=id)
    reservation.delete()
    return redirect('create_reservation')


