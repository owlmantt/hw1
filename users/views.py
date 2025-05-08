from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse_lazy
from django.views.generic import CreateView

class CustomLoginView(LoginView):
    template_name = 'auth/login.html'
    
class CustomLogoutView(LogoutView):
    next_page = '/'

class RegisterView(CreateView):
    form_class = UserCreationForm
    template_name = 'auth/register.html'
    success_url = reverse_lazy('post_list')