from django.shortcuts import render
from django.views.generic.list import ListView

from apps.product.models.product import Product

class HomeView(ListView):
    model = Product
    paginate_by = 10
    context_object_name = 'product_list'
    template_name = 'home/index.html'
