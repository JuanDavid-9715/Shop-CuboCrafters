from django.shortcuts import render, reverse
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.db.models import Q

from ..models.product import Product
from ..models.category import Category
from ..models.promotion import Promotion

from ..forms import ProductForm


class ProductListView(ListView):
    model = Product
    paginate_by = 10
    context_object_name = 'product_list'
    template_name = "product/product/list.html"

    def get_queryset(self):
        field = 'name'
        product_name = self.request.GET.get("product")

        if product_name:
            qs = "MATCH({}) AGAINST('+{}*' IN BOOLEAN MODE)".format(field, product_name)

            return Product.objects.extra(where=[qs])

        return super().get_queryset()

class ProductCreateView(CreateView):
    model = Product
    form_class = ProductForm
    success_url = '/products/'
    template_name = "product/product/create.html"

class ProductUpdateView(UpdateView):
    model = Product
    form_class = ProductForm
    template_name = "product/product/update.html"

    def get_success_url(self):
        return reverse('products') + f"?update=ok,{self.object.name}"

class ProductDeleteView(DeleteView):
    model = Product
    success_url = '/products/'
    template_name = "product/product/delete.html"