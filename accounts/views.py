from django.shortcuts import render
from django.core.urlresolver import reverse_lazy
from django.views.generic import CreateView

from . import forms
# Create your views here.
class SignUp(CreateView):
    form_class = forms.UserCreateForm
    succes_url = reverse_lazy('login')
    template_name = 'accounts/signup.html'