from django import forms
from .widgets import CustomClearableFileInput
from django.forms import Select
from .models import Product, Category, Product_Category


class ProductForm(forms.ModelForm):

    class Meta:
        model = Product
        fields = '__all__'

        image = forms.ImageField(label='Image', required=False, widget=CustomClearableFileInput)

class CategoryForm(forms.ModelForm):

    class Meta:
        model = Category
        categories = Category.objects.all()
        readable_names = [(category.id, category.get_readable_name()) for category in categories]
    
        fields = ['readable_name']
        widgets = {
            'readable_name': Select(choices=readable_names)
        }

class Product_CategoryForm(forms.ModelForm):

    class Meta:
        model = Product_Category
        fields = '__all__'