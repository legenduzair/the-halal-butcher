from django.shortcuts import render, get_object_or_404
from django.contrib import messages

from .models import Profile
from .forms import ProfileForm


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