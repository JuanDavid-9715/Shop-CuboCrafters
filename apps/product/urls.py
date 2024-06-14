from django.urls import path

from .views.categoriesView import CategoryListView, CategoryCreateView, CategoryUpdateView, CategoryDeleteView

urlpatterns = [
    path('categories/', CategoryListView.as_view(), name='categories'),
    path('addCategory/', CategoryCreateView.as_view(), name='addCategory'),
    path('updateCategory/<int:pk>/', CategoryUpdateView.as_view(), name='updateCategory'),
    path('deleteCategory/<int:pk>/', CategoryDeleteView.as_view(), name='deleteCategory'),
]