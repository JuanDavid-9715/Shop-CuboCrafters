from django.urls import path
from .views import SignUpCreateView, LogInView, LogOutView

urlpatterns = [
    path('signUp', SignUpCreateView.as_view(), name='signUp'),
    path('logIn', LogInView.as_view(), name='logIn'),
    path('logOut', LogOutView.as_view(), name='logOut'),
]
