from django.contrib import admin
from catalog.models import Category, Product


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('pk', 'product_name', 'category', 'price',)
    list_filter = ['category']
    search_fields = ['product_name', 'product_description']


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('pk', 'category_name',)
    search_fields = ('category_name',)
