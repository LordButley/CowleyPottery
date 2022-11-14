from django.shortcuts import render

# Create your views here.

def view_bag(request):
    """ A view to return the all products, including sorting queries"""

    context = {
        "apples": 0
    }

    return render(request, 'bag/bag.html', context)