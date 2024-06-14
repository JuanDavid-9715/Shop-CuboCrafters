from django.shortcuts import render, reverse
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.db.models import Q

from ..models.promotion import Promotion

from ..forms import PromotionForm


class PromotionListView(ListView):
    model = Promotion
    paginate_by = 10
    context_object_name = 'promotion_list'
    template_name = "product/promotion/list.html"

    def get_queryset(self):
        promotion_name = self.request.GET.get("promotion")

        if promotion_name:
            return Promotion.objects.filter(Q(name=promotion_name)).distinct()

        return super().get_queryset()

class PromotionCreateView(CreateView):
    model = Promotion
    form_class = PromotionForm
    success_url = '/promotions/'
    template_name = "product/promotion/create.html"

class PromotionUpdateView(UpdateView):
    model = Promotion
    form_class = PromotionForm
    template_name = "product/promotion/update.html"

    def get_success_url(self):
        return reverse('promotions') + f"?update=ok,{self.object.name}"

class PromotionDeleteView(DeleteView):
    model = Promotion
    success_url = '/promotions/'
    template_name = "product/promotion/delete.html"