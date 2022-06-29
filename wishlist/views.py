from django.shortcuts import render, redirect, get_object_or_404, reverse
from products.models import Product

from django.contrib import messages
from .models import Wishlist

# Create your views here.


def view_wishlist(request):

    wishlist = None
    try:
        wishlist = Wishlist.objects.get(user=request.user)
    except Wishlist.DoesNotExist:
        pass

    context = {
        'wishlist': wishlist,
    }

    return render(request, 'wishlist.html', context)


def add_to_wishlist(request, item_id):

    product = get_object_or_404(Product, pk=item_id)
    redirect_url = request.POST.get('redirect_url')

    wish, _ = Wishlist.objects.get_or_create(user=request.user)

    wish.products.add(product)
    messages.info(request, f'{product.name} was added to your wishlist')

    return redirect(redirect_url)


def remove_from_wishlist(request, item_id):
 
    wish = Wishlist.objects.get(user=request.user)
    product = get_object_or_404(Product, pk=item_id)

    # Remove wish from the wishlist
    wish.products.remove(product)
    messages.info(request, f'{product.name} was removed from your wishlist')

    return redirect(reverse('wishlist'))