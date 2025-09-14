from django.urls import reverse_lazy
from django.views.generic import FormView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm


class RgisterUseview(FormView):
    template_name='register.html'
    form_class=UserCreationForm
    success_url=reverse_lazy('home')

    def form_valid(self, form):
        user=form.save()
        login(self.request,user)
        return super().form_valid(form)
    