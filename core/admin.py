from django.contrib import admin

from .models import Category, Product


class ProductAdmin(admin.ModelAdmin):
    list_display = ["category", "created_by", "stock", "name"]


admin.site.register(Category)
admin.site.register(Product, ProductAdmin)

