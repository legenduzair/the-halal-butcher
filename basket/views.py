"""System Module"""
from django.shortcuts import render, redirect, get_object_or_404
from django.shortcuts import reverse, HttpResponse
from django.contrib import messages
from products.models import Product

# Create your views here.


def view_basket(request):

    """View to access users basket"""
    context = {}

    return render(request, 'basket.html', context)


def add_to_basket(request, item_id):

    """View to add product to basket"""

    product = get_object_or_404(Product, pk=item_id)
    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    basket = request.session.get('basket', {})

    if item_id in list(basket.keys()):
        basket[item_id] += quantity
        messages.success(request, f'Updated {product.name} quantity \
             to {basket[item_id]}')
    else:
        basket[item_id] = quantity
        messages.success(request, f'Added {basket[item_id]} x {product.name} \
             to your basket')

    request.session['basket'] = basket
    return redirect(redirect_url)


def adjust_basket(request, item_id):

    """View to edit product in basket"""

    product = get_object_or_404(Product, pk=item_id)
    quantity = int(request.POST.get('quantity'))
    basket = request.session.get('basket', {})

    if quantity > 0:
        basket[item_id] = quantity
        messages.success(request, f'Updated {product.name} \
             quantity to {basket[item_id]}')
    else:
        basket.pop(item_id)
        messages.success(request, f'Removed {product.name} from your basket')

    request.session['basket'] = basket
    return redirect(reverse('view_basket'))


def remove_from_basket(request, item_id):

    """View to remove product from basket"""

    try:
        product = get_object_or_404(Product, pk=item_id)
        basket = request.session.get('basket', {})

        basket.pop(item_id)
        messages.success(request, f'Removed {product.name} from your basket')

        request.session['basket'] = basket
        return HttpResponse(status=200)

    except Exception as e:
        messages.error(request, f'Error removing item: {e}')
        return HttpResponse(status=500)
