from django.shortcuts import render, redirect, reverse, get_object_or_404, HttpResponse
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST
from django.contrib import messages
from django.conf import settings

from .forms import Order, OrderForm
from checkout.models import OrderLineItem
from products.models import Product
from profiles.forms import ProfileForm
from profiles.models import Profile
from basket.contexts import basket_contents

import stripe
import json

# Create your views here.


@login_required
@require_POST
def cache_checkout_data(request):
    try:
        pid = request.POST.get('client_secret').split('_secret')[0]
        stripe.api_key = settings.STRIPE_SECRET_KEY
        stripe.PaymentIntent.modify(pid, metadata={
            'basket': json.dumps(request.session.get('basket', {})),
            'save_info': request.POST.get('save_info'),
            'username': request.user,
        })
        return HttpResponse(status=200)
    except Exception as e:
        messages.error(request, 'Sorry your payment cannot be \
            processed right now. Please try again later.')
        return HttpResponse(content=e, status=400)


@login_required
def checkout(request):

    stripe_public_key = settings.STRIPE_PUBLIC_KEY
    stripe_secret_key = settings.STRIPE_SECRET_KEY

    if request.method == 'POST':
        basket = request.session.get('basket', {})
        form_data = {
            'first_name': request.POST['first_name'],
            'last_name': request.POST['last_name'],
            'email': request.POST['email'],
            'phone_number': request.POST['phone_number'],
            'street_address': request.POST['street_address'],
            'town_or_city': request.POST['town_or_city'],
            'county': request.POST['county'],
            'postcode': request.POST['postcode'],
            'country': request.POST['country'],
        }
        order_form = OrderForm(form_data)
        if order_form.is_valid():
            order = order_form.save(commit=False)
            pid = request.POST.get('client_secret').split('_secret')[0]
            order.stripe_pid = pid
            order.original_basket = json.dumps(basket)
            order.save()
            for item_id, item_data in basket.items():
                try:
                    product = Product.objects.get(id=item_id)
                    if isinstance(item_data, int):
                        order_line_item = OrderLineItem(
                            order=order,
                            product=product,
                            quantity=item_data,
                        )
                        order_line_item.save()
                except Product.DoesNotExist:
                    messages.error(request, (
                        'One of the products in your basket was not found in our \
                            database. Please contact us for assistance!'
                    ))
                    order.delete()
                    return redirect(reverse('view_basket'))
            request.session['save_info'] = 'save-info' in request.POST
            return redirect(reverse('checkout_success',
                                    args=[order.order_number]))
        else:
            messages.error(request, 'There was an error with your form. \
                Please double check your information.')
    else:
        basket = request.session.get('basket', {})
        if not basket:
            messages.error(request, 'There are no items in your basket at the moment.')
            return redirect(reverse('products'))

        current_basket = basket_contents(request)
        total = current_basket['grand_total']
        stripe_total = round(total * 100)
        stripe.api_key = stripe_secret_key
        intent = stripe.PaymentIntent.create(
            amount=stripe_total,
            currency=settings.STRIPE_CURRENCY,
        )

        if request.user.is_authenticated:
            try:
                profile = Profile.objects.get(user=request.user)
                order_form = OrderForm(initial={
                    'first_name': profile.first_name,
                    'last_name': profile.last_name,
                    'phone_number': profile.phone_number,
                    'street_address': profile.street_address,
                    'country': profile.country,
                    'postcode': profile.postcode,
                    'town_or_city': profile.town_or_city,
                    'county': profile.county,
                    'email': profile.user.email,
                })
            except Profile.DoesNotExist:
                order_form = OrderForm()
        else:
            order_form = OrderForm()

    if not stripe_public_key:
        messages.warning(request, 'Stipe public key is missing, set in env variables')

    template = 'checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': stripe_public_key,
        'client_secret': intent.client_secret,
    }

    return render(request, template, context)


@login_required
def checkout_success(request, order_number):

    save_info = request.session.get('save_info')
    order = get_object_or_404(Order, order_number=order_number)

    if request.user.is_authenticated:
        profile = Profile.objects.get(user=request.user)

        order.user_profile = profile
        order.save()

        # Save the user's info
        if save_info:
            profile_data = {
                'first_name': order.first_name,
                'last_name': order.last_name,
                'phone_number': order.phone_number,
                'street_address': order.street_address,
                'town_or_city': order.town_or_city,
                'county': order.county,
                'postcode': order.postcode,
                'country': order.country,
                'email_address': order.email,
            }
            profile_form = ProfileForm(profile_data, instance=profile)
            if profile_form.is_valid():
                profile_form.save()

    messages.success(request, f'Order successfully processed! \
        Your order number is {order_number}. A confirmation \
        email will be sent to {order.email}')
    
    if 'basket' in request.session:
        del request.session['basket']

    template = 'checkout_success.html'
    context = {
        'order': order,
    }
    return render(request, template, context)

