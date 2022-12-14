from django import template


register = template.Library()

@register.filter(name='calc_subtotal')
def calc_subtotal(price, quantity):
    return price * quantity

@register.filter(name='stock_left')
def stock_left(stock_dict, product):
    if product.id in stock_dict:
        return stock_dict[product.id]
    else:
        return product.stock
        