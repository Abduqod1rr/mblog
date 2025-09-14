from django.urls import reverse_lazy
from django.views.generic import FormView  
from django.contrib.auth import login
from django.contrib.auth.views import LoginView,LogoutView 
from django.contrib.auth.forms import UserCreationForm 


class RegisterUseview(FormView):
    template_name='register.html'
    form_class=UserCreationForm
    success_url=reverse_lazy('home')

    def form_valid(self, form):
        user=form.save()
        login(self.request,user)
        return super().form_valid(form)

class LoginUserView(LoginView):
    template_name='login.html'
    redirect_authenticated_user=True
    def get_success_url(self) -> str:
        return self.get_redirect_url() or reverse_lazy('home')