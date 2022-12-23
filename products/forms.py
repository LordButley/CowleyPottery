from django import forms
from django.forms import Select
from .models import Product, Category, Product_Category


class ProductForm(forms.ModelForm):

    class Meta:
        model = Product
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'border-black rounded-0'


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