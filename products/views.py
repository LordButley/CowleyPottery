from django.shortcuts import render
from .models import Product, Product_Category

# Create your views here.

def shop(request):
    """ A view to return the landing page """
    
    products = Product.objects.all()
    product_categories = Product_Category.objects.all()

    context = {
        'products': products,
        'product_categories': product_categories,
    }

    return render(request, 'products/products.html', context)

