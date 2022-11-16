from django.shortcuts import render, get_object_or_404
from .models import Product, Product_Category, Category
from datetime import datetime, timedelta

# Create your views here.

def shop(request):
    """ A view to return the shop landing page """
    
    categories = Category.objects.all()

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
            if 'new' in categories:
                # product_categories = "Check"
                product_categories = product_categories.exclude(product__date_added__lt = (datetime.today() - timedelta(weeks=4)))
            else:
                product_categories = product_categories.filter(category__name__in=categories)

    context = {
        'product_categories': product_categories,
    }

    return render(request, 'products/products.html', context)

def view_product(request, product_id):
    """ A view to return the all products, including sorting queries"""

    product = get_object_or_404(Product, pk=product_id)
 
    context = {
        'product': product,
    }

    return render(request, 'products/view_product.html', context)


