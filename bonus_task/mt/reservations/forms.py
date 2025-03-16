from django import forms
from .models import Reservation

class ReservationForm(forms.ModelForm):
    class Meta:
        model = Reservation
        fields = ['customer', 'table', 'date', 'status']
# forms.py
from django import forms

class AdminLoginForm(forms.Form):
    password = forms.CharField(widget=forms.PasswordInput, label="Пароль")
