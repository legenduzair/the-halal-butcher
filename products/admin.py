from django.contrib import admin
from .models import Product, Category
from django_summernote.admin import SummernoteModelAdmin


class ProductAdmin(SummernoteModelAdmin):
    summernote_fields = ('description', 'additional_information',)
    list_display = (
        'sku',
        'name',
        'meat_category',
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


admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)