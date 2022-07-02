from django.shortcuts import render, redirect, reverse
from django.contrib import messages

from .forms import OrderForm

# Create your views here.


def checkout(request):

    basket = request.session.get('basket', {})
    if not basket:
        messages.error(request, 'There are no items in your basket at the moment.')
        return redirect(reverse('products'))

    order_form = OrderForm()
    template = 'checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': 'pk_test_51L7Jk3EEYiOGw3IXl1FXLtlRCAPQJvx2HdLxSY2zbDc3mYxjGJYMI1K9DA0CYWhgzfyj9xnedrHPNRBbWxEVDf5H007NayRIHc',
        'client_secret': 'test client secret',
    }

    return render(request, template, context)
