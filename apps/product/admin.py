from django.contrib import admin

from .models.category import Category
from .models.promotion import Promotion
from .models.product import Product

@admin.register(Category)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ("name", "description")
    search_fields = ("name__startswith", )

@admin.register(Promotion)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ("name", "price", "discount", "description")
    search_fields = ("name__startswith", )

@admin.register(Product)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ("name", "price", "description")
    search_fields = ("name__startswith", )