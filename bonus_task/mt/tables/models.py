from django.db import models

class Table(models.Model):
    number = models.IntegerField(unique=True)
    seats = models.IntegerField()
    is_available = models.BooleanField(default=True)

    def __str__(self):
        return f"Table {self.number} - Seats: {self.seats}"
# forms.py
from django import forms

class AdminLoginForm(forms.Form):
    password = forms.CharField(widget=forms.PasswordInput, label="Пароль")
