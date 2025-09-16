from django.db.models.query import QuerySet
from django.forms import BaseModelForm
from django.shortcuts import render ,HttpResponse,redirect
from .models import Post ,Comment
from django.views.generic import DeleteView,ListView ,CreateView 
from django.contrib.auth.mixins import LoginRequiredMixin ,UserPassesTestMixin
from django.urls import reverse_lazy
from typing import cast

class Homeview(ListView):
    model=Post
    template_name='home.html'
    context_object_name='post'

    def get_queryset(self) :
        query=self.request.GET.get('q')
        if query:
            return Post.objects.filter(title__icontains=query) | Post.objects.filter(text__icontains=query)
        return Post.objects.all()

class AddCommentView(LoginRequiredMixin,CreateView):
    model=Comment
    fields=['comment']
    success_url=reverse_lazy('home')

    def form_valid(self, form):
        form.instance.user=self.request.user
        form.instance.post=Post.objects.get(pk=self.kwargs['post_pk'])
        return super().form_valid(form)
        
 
class DeleteCommentView(LoginRequiredMixin,UserPassesTestMixin,DeleteView):
    model=Comment
    success_url=reverse_lazy('home')

    def test_func(self) :
        obj=cast(Comment,self.get_object())
        return obj.user==self.request.user

