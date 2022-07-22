from django.contrib import admin
from .models import Product, Category, ProductReview


class ProductAdmin(admin.ModelAdmin):
    list_display = (
        'sku',
        'name',
        'meat_category',
        'description',
        'additional_information',
        'price',
        'rating',
        'image',
    )

    ordering = ('sku',)


class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        'friendly_name',
        'name',
    )


class ProductReviewAdmin(admin.ModelAdmin):
    '''Register of Review model'''
    list_display = (
        'user',
        'product',
        'content',
        'rating',
    )


admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(ProductReview, ProductReviewAdmin)
