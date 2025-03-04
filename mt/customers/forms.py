from django import forms
from .models import Customer

class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ['name', 'phone']
# forms.py
from django import forms

class AdminLoginForm(forms.Form):
    password = forms.CharField(widget=forms.PasswordInput, label="Пароль")
