from django.shortcuts import render, redirect
from django.views.generic import FormView
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth import login, authenticate

from .forms import SignUpForm
from .models import Profile

class SignUpView(FormView):
    model = Profile
    form_class = SignUpForm
    template_name = 'account/signUp.html'

    def form_valid(self, form):
        form.save()

        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password1')

        username = authenticate(
            username = username,
            password = password
        )
        login(self.request, username)

        return redirect('/')

class LogInView(LoginView):
    template_name = 'account/logIn.html'

class LogOutView(LogoutView):
    pass