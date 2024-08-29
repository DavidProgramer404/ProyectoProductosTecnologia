from django import forms
from .models import Producto

# class

class ProductoForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = '__all__'