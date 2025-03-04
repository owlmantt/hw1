from django.urls import path
from . import views
from django.urls import path
from .views import create_table, table_edit, table_delete

urlpatterns = [
    path('create/', create_table, name='create_table'),
    path('<int:id>/edit/', table_edit, name='table_edit'),
    path('', views.home, name='home'),
    path('admin_login/', views.admin_login, name='admin_login'),  # Путь для входа как администратор
    path('', views.home, name='home'),  # Главная страница
    path('<int:id>/delete/', table_delete, name='table_delete'),
]
