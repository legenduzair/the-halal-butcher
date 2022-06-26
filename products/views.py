from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.contrib import messages
from django.db.models import Q
from .models import Product
# Create your views here.


def product_list(request):

    products = Product.objects.all()
    query = None

    if 'q' in request.GET:
        query = request.GET['q']
        if not query:
            messages.error(request, "You didn't enter any search criteria!")
            return redirect(reverse('products'))

        queries = (Q(name__icontains=query) | 
                   Q(description__icontains=query) |
                   Q(additional_information__icontains=query))
        products = products.filter(queries)

    context = {
        'products': products,
        'search_query': query,
    }

    return render(request, 'products.html', context)


def product_detail(request, product_id):

    product = get_object_or_404(Product, pk=product_id)

    context = {
        'product': product,
    }

    return render(request, 'product_detail.html', context)