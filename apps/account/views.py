from django.shortcuts import render, redirect
from django.views.generic import FormView

from .forms import SignUpForm
from .models import Profile

class SignUpView(FormView):
    model = Profile
    form_class = SignUpForm
    template_name = 'account/signUp.html'

    def form_valid(self, form):
        form.save()

        return redirect('/')
