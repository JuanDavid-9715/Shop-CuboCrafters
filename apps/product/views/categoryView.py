from django.shortcuts import render, reverse
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.db.models import Q

from ..models.category import Category

from ..forms import CategoryForm


class CategoryListView(ListView):
    model = Category
    paginate_by = 10
    context_object_name = 'category_list'
    template_name = "product/category/list.html"

    def get_queryset(self):
        field = 'name'
        category_name = self.request.GET.get("category")

        if category_name:
            qs = "MATCH({}) AGAINST('+{}*' IN BOOLEAN MODE)".format(field, category_name)

            return Category.objects.extra(where=[qs])

        return super().get_queryset()

class CategoryCreateView(CreateView):
    model = Category
    form_class = CategoryForm
    success_url = '/categories/'
    template_name = "product/category/create.html"

class CategoryUpdateView(UpdateView):
    model = Category
    form_class = CategoryForm
    template_name = "product/category/update.html"

    def get_success_url(self):
        return reverse('categories') + f"?update=ok,{self.object.name}"

class CategoryDeleteView(DeleteView):
    model = Category
    success_url = '/categories/'
    template_name = "product/category/delete.html"