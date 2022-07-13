from django.shortcuts import render, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Profile
from .forms import ProfileForm

from checkout.models import Order


@login_required
def profile(request):

    profile = get_object_or_404(Profile, user=request.user)
    form = ProfileForm(request.POST, instance=profile)
    if request.method == 'POST':
        form = ProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            messages.success(request, 'Profile updated successfully')
        else:
            messages.error(request, 'Update failed. \
                Please ensure the form is correct')
    else:
        form = ProfileForm(instance=profile)
    
    orders = profile.orders.all()
    template = 'profiles.html'
    context = {
        'form': form,
        'orders': orders,
        'on_profile_page': True
    }

    return render(request, template, context)


@login_required
def order_history(request, order_number):
    order = get_object_or_404(Order, order_number=order_number)

    messages.success(request, (
        f'This is a past confirmation for order number {order_number}.'
        'A confirmation email was sent on the order date'
    ))

    template = 'checkout_success.html'
    context = {
        'order': order,
        'from_profile': True
    }
    return render(request, template, context)