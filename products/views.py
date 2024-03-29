from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.db.models.functions import Lower
from .models import Product, Category, ProductReview
from .forms import ProductForm, ReviewForm
# Create your views here.


def product_list(request):

    products = Product.objects.all()
    query = None
    categories = None
    sort = None
    direction = None

    if request.GET:
        if 'sort' in request.GET:
            sortkey = request.GET['sort']
            sort = sortkey
            if sortkey == 'name':
                sortkey = 'lower_name'
                products = products.annotate(lower_name=Lower('name'))

            if 'direction' in request.GET:
                direction = request.GET['direction']
                if direction == 'desc':
                    sortkey = f'-{sortkey}'
            products = products.order_by(sortkey)

        if 'category' in request.GET:
            categories = request.GET['category'].split(',')
            products = products.filter(meat_category__name__in=categories)
            categories = Category.objects.filter(name__in=categories)

        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(request, "You didn't enter any search criteria")
                return redirect(reverse('products'))

            queries = (Q(name__icontains=query) |
                       Q(description__icontains=query) |
                       Q(additional_information__icontains=query))
            products = products.filter(queries)

    current_sorting = f'{sort}_{direction}'

    context = {
        'products': products,
        'search_query': query,
        'current_categories': categories,
        'current_sorting': current_sorting,
    }

    return render(request, 'products.html', context)


def product_detail(request, product_id):

    product = get_object_or_404(Product, pk=product_id)
    form = ReviewForm
    reviews = product.reviews.filter()

    context = {
        'product': product,
        'form': form,
        'reviews': reviews,
    }

    return render(request, 'product_detail.html', context)


@login_required
def add_product(request):

    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            product = form.save()
            messages.success(request, 'Product added successfully')
            return redirect(reverse('product_detail', args=[product.id]))
        else:
            messages.error(request, 'There is an error in the form.')
    else:
        form = ProductForm()

    context = {
        'form': form
    }

    return render(request, 'add_product.html', context)


@login_required
def edit_product(request, product_id):

    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    product = get_object_or_404(Product, pk=product_id)
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            messages.success(request, 'Product updated successfully')
            return redirect(reverse('product_detail', args=[product.id]))
        else:
            messages.error(request, 'There is an error in the form.')
    else:
        form = ProductForm(instance=product)
        messages.info(request, f'You are editing {product.name}')

    template = 'edit_product.html'
    context = {
        'form': form,
        'product': product,
    }

    return render(request, template, context)


@login_required
def delete_product(request, product_id):

    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    product = get_object_or_404(Product, pk=product_id)
    if request.method == 'POST':
        product.delete()
        messages.success(request, 'Product deleted successfully')
        return redirect(reverse('products'))

    template = 'delete_product.html'
    context = {
        "product": product,
    }

    return render(request, template, context)


def render_reviews(request):
    """ A view to render all reviews """
    reviews = ProductReview.objects.all()
    form = ReviewForm()

    context = {'reviews': reviews, 'review_form': form}
    return render(request, 'product_detail.html', context)


@login_required
def add_review(request, product_id):

    product = get_object_or_404(Product, pk=product_id)
    if request.method == 'POST':
        review_form = ReviewForm(request.POST or None)
        if review_form.is_valid():
            data = review_form.save(commit=False)
            data.user = request.user
            data.product = product
            data.save()
            messages.success(request, 'Your review was posted successfully!')
            return redirect(reverse('product_detail',
                                    args=[product.id]))
        else:
            form = ReviewForm()
            messages.error(request,
                           'Failed to add your review,n\
                            please ensure the form is valid')

    context = {'form': form}

    return render(request, context)


@login_required
def edit_review(request, review_id):

    review = get_object_or_404(ProductReview, pk=review_id)
    product = review.product
    if request.method == 'POST':
        form = ReviewForm(request.POST, instance=review)
        if form.is_valid():
            form.save()
            messages.info(request, 'Your review has been updated successfully')
            return redirect(reverse('product_detail',
                            args=[product.id]))
        else:
            messages.error(request, 'Failed to update your review,n\
                            please ensure the form is valid')

    else:
        form = ReviewForm(instance=review)
        messages.info(request, 'You are updating your review')

    template = 'product_detail.html'
    context = {
        'form': form,
        'review': review,
        'product': product,
        'edit': True,
    }
    return render(request, template, context)


def delete_review(request, review_id):

    review = get_object_or_404(ProductReview, pk=review_id)
    product = review.product
    review.delete()
    messages.success(request, 'Your review has been deleted!')
    return redirect(reverse('product_detail', args=[product.id]))
