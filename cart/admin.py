from django.contrib import admin
from .models import CartOrder, CartOrderItems, Address

class CartOrderAdmin(admin.ModelAdmin):
    list_display = ('user', 'price', 'paid_status', 'product_status', 'order_date')

class CartOrderItemsAdmin(admin.ModelAdmin):
    list_display = ('order', 'invoice_num', 'qty', 'price', 'total')

class AddressAdmin(admin.ModelAdmin):
    list_display = ('user', 'address', 'status')

admin.site.register(CartOrder, CartOrderAdmin)
admin.site.register(CartOrderItems, CartOrderItemsAdmin)
admin.site.register(Address, AddressAdmin)
