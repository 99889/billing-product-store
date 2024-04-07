# forms.py
from django import forms
from django.forms import inlineformset_factory
from .models import Product, Sale, SaleItem
from django.contrib.auth import get_user_model

Customer = get_user_model()

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'price', 'description']

class SaleForm(forms.ModelForm):
    class Meta:
        model = Sale
        fields = ['customer']

# Define a formset for sale items
SaleItemFormSet = inlineformset_factory(Sale, SaleItem, fields=('product', 'quantity'), extra=1)

from django.contrib.auth import get_user_model

User = get_user_model()

class CustomerForm(forms.ModelForm):
    class Meta:
        model = User  # Assuming you're using the default User model
        fields = ['first_name', 'last_name', 'email']
