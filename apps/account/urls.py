from django.urls import path
from .views import SignUpView

urlpatterns = [
    path('signUp', SignUpView.as_view(), name='signUp')
]