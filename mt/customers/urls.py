from django.urls import path
from .views import create_customer, customer_edit, customer_delete

urlpatterns = [
    path('create/', create_customer, name='create_customer'),
    path('<int:id>/edit/', customer_edit, name='customer_edit'),
    path('<int:id>/delete/', customer_delete, name='customer_delete'),
]
