from decimal import Decimal
from django.conf import settings
from products.models import Product
from django.shortcuts import get_object_or_404

def bag_contents(request):

    bag_items = []
    total = 0
    product_count = 0
    bag = request.session.get('bag', {})
    # stock_check_objects = Product.objects.all()
    # stock_check = {}
    # for item in stock_check_objects:
    #     stock_check.update({item.id: item.stock})

    for product_id, quantity in bag.items():
        product = get_object_or_404(Product, pk=product_id)
        # stock_check[int(product_id)] = stock_check[int(product_id)] - quantity
        total += quantity * product.price
        stock_left = product.stock - quantity
        product_count += quantity
        bag_items.append({
            'product_id': product_id,
            'quantity': quantity,
            'product': product,
            'stock_left': stock_left,
        })


    if total < settings.FREE_DELIVERY_THRESHOLD:
        delivery = settings.STANDARD_DELIVERY_COST
        free_delivery_delta = settings.FREE_DELIVERY_THRESHOLD - total
    else:
        delivery = 0
        free_delivery_delta = 0
    
    grand_total = delivery + total
    
    context = {
        'bag_items': bag_items,
        'total': total,
        'product_count': product_count,
        'delivery': delivery,
        'free_delivery_delta': free_delivery_delta,
        'free_delivery_threshold': settings.FREE_DELIVERY_THRESHOLD,
        # 'stock_check': stock_check,
        'grand_total': grand_total,
    }

    return context
