from django.shortcuts import render

# Create your views here.


def view_wishlist(request):

    context = {}

    return render(request, 'wishlist.html', context)