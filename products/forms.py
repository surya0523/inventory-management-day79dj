from django import forms
from .models import Product

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'price', 'description', 'in_stock']
        # Optionally customize widgets for better UI
        widgets = {
            'description': forms.Textarea(attrs={'rows': 4}),
        }