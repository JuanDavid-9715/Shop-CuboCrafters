from django.contrib import admin

from .models.categories import Categories
from .models.promotions import Promotions
from .models.products import Products

@admin.register(Categories)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ("name", "description")
    search_fields = ("name__startswith", )

@admin.register(Promotions)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ("name", "price", "discount", "description")
    search_fields = ("name__startswith", )

@admin.register(Products)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ("name", "price", "description")
    search_fields = ("name__startswith", )