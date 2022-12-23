from django.shortcuts import render, get_object_or_404
from .models import Product, Product_Category, Category
from datetime import datetime, timedelta
from django.contrib import messages
from .forms import ProductForm, CategoryForm, Product_CategoryForm


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
    print(product_id)
    product = get_object_or_404(Product, pk=int(product_id))
 
    context = {
        'product': product,
    }

    return render(request, 'products/view_product.html', context)


def add_product(request):
    """ Add a product to the store """

    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            category_id = request.POST.get('readable_name')
            category = Category.objects.get(id=category_id)

            # get your category here first and define it as category
            form.save()
            print(form)
            Product_Category.objects.create(category=category, product=form.instance)
            # directly create a Product_Category object here
            # something along the lines of Product_Category.objects.create(category=category, product=form)
            messages.success(request, 'Successfully added product')

            print('readable_name')
            print(type(category))
            # product_category = Product_CategoryForm()
            # product_category.category = category
        else:
            messages.error(request, 'Failed to add product. Please ensure the form is valid')
            return redirect(reverse('add_product'))
    else:
        form = ProductForm()
    category_form = CategoryForm()
    template = 'products/add_product.html'
    context = {
        'form': form,
        'category_form': category_form,
    }

    return render(request, template, context)

def edit_product(request, product_id):
    """ Edit a product in the store """
    product = get_object_or_404(Product, pk=product_id)
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully updated product!')
            return redirect(reverse('product_detail', args=[product.id]))
        else:
            messages.error(request, 'Failed to update product. Please ensure the form is valid.')
    else:
        form = ProductForm(instance=product)
        messages.info(request, f'You are editing {product.name}')

    template = 'products/edit_product.html'
    context = {
        'form': form,
        'product': product,
    }

    return render(request, template, context)