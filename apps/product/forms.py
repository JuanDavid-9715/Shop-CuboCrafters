from django import forms

from .models.category import Category
from .models.promotion import Promotion
from .models.product import Product

class CategoryForm(forms.ModelForm):
    
    class Meta:
        model = Category
        fields = "__all__"

class PromotionForm(forms.ModelForm):
    
    class Meta:
        model = Promotion
        fields = "__all__"


class ProductForm(forms.ModelForm):
    
    class Meta:
        model = Product
        fields = "__all__"

