from django.contrib import admin
from shop.models import Category, Product

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "slug")
    list_display_links = ("title", )
    prepopulated_fields = {"slug": ("title", )}

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "author")
    list_display_links = ("title", )
    prepopulated_fields = {"slug": ("title", )}