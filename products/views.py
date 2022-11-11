from django.shortcuts import render
from .models import Product, Product_Category, Category

# Create your views here.

def shop(request):
    """ A view to return the shop landing page """
    
    # products = Product.objects.all()
    categories = Category.objects.all()
    # product_categories = Product_Category.objects.all()

    context = {
        # 'products': products,
        'categories': categories,
        # 'product_categories': product_categories,
    }

    return render(request, 'products/shop.html', context)

def all_products(request):
    """ A view to return the all products, including sorting queries"""

    product_categories = Product_Category.objects.all()
    # products = Product.objects.all()

    if request.GET:
        if 'category' in request.GET:
            categories = request.GET['category'].split(',')
            product_categories = product_categories.filter(category__name__in=categories)
            # categories = Category.objects.filter(name__in=categories)

    context = {
        'product_categories': product_categories,
    }

    return render(request, 'products/products.html', context)

