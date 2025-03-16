from django import forms
from .models import Table

class TableForm(forms.ModelForm):
    class Meta:
        model = Table
        fields = ['number', 'seats', 'is_available']
        widgets = {
            'number': forms.NumberInput(attrs={'class': 'form-control'}),
            'seats': forms.NumberInput(attrs={'class': 'form-control'}),
            'is_available': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }
# forms.py (в папке tables)
# forms.py

from django import forms

class AdminLoginForm(forms.Form):
    password = forms.CharField(widget=forms.PasswordInput, label="Пароль")
