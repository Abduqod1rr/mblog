from django.forms import BaseModelForm
from django.shortcuts import render ,HttpResponse,redirect
from .models import Post ,Comment
from django.views.generic import DeleteView,ListView ,CreateView 
from django.contrib.auth.mixins import LoginRequiredMixin 
from django.urls import reverse_lazy

class Homeview(ListView):
    model=Post
    template_name='home.html'
    context_object_name='post'

class AddCommentView(LoginRequiredMixin,CreateView):
    model=Comment
    fields=['comment']
    success_url=reverse_lazy('home')

    def form_valid(self, form):
        form.instance.user=self.request.user
        form.instance.post=Post.objects.get(pk=self.kwargs['post_pk'])
        return super().form_valid(form)
        
 


