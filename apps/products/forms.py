from django import forms

class CategoriesForm(forms.ModelForm):
    
    class Meta:
        model = Categories
        fields = "__all__"

class PromotionsForm(forms.ModelForm):
    
    class Meta:
        model = Promotions
        fields = "__all__"


class ProductsForm(forms.ModelForm):
    
    class Meta:
        model = Products
        fields = "__all__"

