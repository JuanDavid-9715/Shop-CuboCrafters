from django.urls import path

from .views.categoryView import CategoryListView, CategoryCreateView, CategoryUpdateView, CategoryDeleteView
from .views.promotionView import PromotionListView, PromotionCreateView, PromotionUpdateView, PromotionDeleteView

urlpatterns = [
    #urls Category
    path('categories/', CategoryListView.as_view(), name='categories'),
    path('addCategory/', CategoryCreateView.as_view(), name='addCategory'),
    path('updateCategory/<int:pk>/', CategoryUpdateView.as_view(), name='updateCategory'),
    path('deleteCategory/<int:pk>/', CategoryDeleteView.as_view(), name='deleteCategory'),

    #urls Promotion
    path('promotions/', PromotionListView.as_view(), name='promotions'),
    path('addPromotion/', PromotionCreateView.as_view(), name='addPromotion'),
    path('updatePromotion/<int:pk>/', PromotionUpdateView.as_view(), name='updatePromotion'),
    path('deletePromotion/<int:pk>/', PromotionDeleteView.as_view(), name='deletePromotion'),

]