from django.contrib import admin

from core.models import Category, Product
from django.utils.html import format_html
# Register your models here.


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')
    search_fields = ('name',)

class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'price', 'stock', 'created_at', 'display_image')
    list_filter = ('category', 'created_at')
    search_fields = ('name', 'category__name')
    autocomplete_fields = ['category']

    def display_image(self, obj):
        if obj.image:
            return format_html('<img src="{}" style="width: 50px; height: auto;" />', obj.image.url)
        return "No Image"

# Register the models with their custom admin classes
admin.site.register(Category, CategoryAdmin)
admin.site.register(Product, ProductAdmin)
