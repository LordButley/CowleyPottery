from django.contrib import admin
from .models import Product, Category, Product_Category

# Register your models here.

class ProductAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'price',
        'stock',
        'image',
    )

class ProductCategoryAdmin(admin.ModelAdmin):
    list_display = (
        'category',
        'product',
    )


admin.site.register(Product, ProductAdmin)
admin.site.register(Category)
admin.site.register(Product_Category, ProductCategoryAdmin)