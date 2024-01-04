from django.urls import reverse_lazy
from django.views.generic import CreateView

from apps.accounts.forms import UserSignUpForm


class SignUpUser(CreateView):
    form_class = UserSignUpForm
    template_name = 'registration/singup.html'
    success_url = reverse_lazy('login')
