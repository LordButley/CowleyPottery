from django.shortcuts import render, redirect, reverse, HttpResponse, get_object_or_404
from django.contrib import messages
from products.models import Product
# Create your views here.

def view_bag(request):
    """ A view to return the all products, including sorting queries"""

    return render(request, 'bag/bag.html')


def add_to_bag(request, product_id):
    """ Add a quantity of the specified product to the shopping bag """

    product = get_object_or_404(Product, pk=product_id)
    # product = Product.objects.get(pk=product_id)
    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    print(redirect_url)
    bag = request.session.get('bag', {})

    if product_id in list(bag.keys()):
        bag[product_id] += quantity
        print(quantity)
        messages.success(request, f'Updated {product.name} quantity to {bag[product_id]}')

    else:
        bag[product_id] = quantity
        messages.success(request, f'Added {product.name} to your bag')

    request.session['bag'] = bag
    return redirect(redirect_url)


def adjust_bag(request, product_id):
    """Adjust the quantity of the specified product to the specified amount"""
    
    # print("called")
    product = get_object_or_404(Product, pk=product_id)
    quantity = int(request.POST.get('quantity'))
    bag = request.session.get('bag', {})

    if quantity > 0:
        bag[product_id] = quantity
        messages.success(request, f'Updated {product.name} quantity to {bag[product_id]}')
    else:
        bag.pop(product_id)
        messages.success(request, f'Removed {product.name} from your bag')


    request.session['bag'] = bag
    return redirect(reverse('view_bag'))


def remove_from_bag(request, product_id):
    """Remove the item from the shopping bag"""
    
    try:
        product = get_object_or_404(Product, pk=product_id)
        bag = request.session.get('bag', {})
        bag.pop(product_id)

        request.session['bag'] = bag
        messages.success(request, f'Removed {product.name} from your bag')
        return HttpResponse(status=200)

    except Exception as e:
        messages.error(request, f'Error removing item: {e}')
        return HttpResponse(status=500)