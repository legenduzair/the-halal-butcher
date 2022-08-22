from django.contrib import admin
from .models import Order, OrderLineItem


class OrderLineItemAdminInline(admin.TabularInline):
    model = OrderLineItem
    readonly_fields = ('lineitem_total',)


class OrderAdmin(admin.ModelAdmin):
    inlines = (OrderLineItemAdminInline,)

    readonly_fields = ('order_number', 'date',
                       'order_total', 'shipping_costs',
                       'grand_total', 'original_basket', 'stripe_pid')

    fields = ('order_number', 'user_profile', 'first_name', 'last_name',
              'email', 'phone_number', 'street_address', 'town_or_city',
              'county', 'postcode', 'country', 'date',
              'shipping_costs', 'order_total', 'grand_total',
              'original_basket', 'stripe_pid',)

    list_display = ('order_number', 'date', 'first_name',
                    'last_name', 'order_total', 'grand_total',)

    ordering = ('-date',)


admin.site.register(Order, OrderAdmin)
