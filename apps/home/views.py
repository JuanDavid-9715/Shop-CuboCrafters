from django.shortcuts import render
from django.views.generic.list import ListView

from apps.product.models.category import Category
from apps.product.models.product import Product
from apps.product.models.promotion import Promotion

class HomeView(ListView):
    model = Category
    paginate_by = 4
    context_object_name = 'category_list'
    template_name = 'home/index.html'

    def get_context_data(self, *args, **kwargs):
        context = super(ListView, self).get_context_data(**kwargs)
        context['product_list'] = Product.objects.all()
        context['promotion_list'] = Promotion.objects.all()
        return context
