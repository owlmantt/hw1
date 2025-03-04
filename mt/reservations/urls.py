from django.urls import path
from .views import create_reservation, reservation_edit, reservation_delete

urlpatterns = [
    path('create/', create_reservation, name='create_reservation'),
    path('<int:id>/edit/', reservation_edit, name='reservation_edit'),
    path('<int:id>/delete/', reservation_delete, name='reservation_delete'),
]
