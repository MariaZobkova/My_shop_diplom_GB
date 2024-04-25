from django.contrib import admin
from goods.models import Categories, Products


@admin.register(Categories)
class CategoriesAdmin(admin.ModelAdmin):
    list_display = ["name",]


@admin.register(Products)
class ProductsAdmin(admin.ModelAdmin):
    list_display = ["name", "count", "price"]
    search_fields = ["name", "description"]
    list_filter = ["count", "category"]
    fields = [
        "name",
        "category",
        "description",
        "image",
        "price",
        "count",
    ]
