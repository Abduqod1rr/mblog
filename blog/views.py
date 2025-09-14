from django.shortcuts import render ,HttpResponse
from .models import Post
from django.views.generic import DeleteView,ListView ,CreateView
# Create your views here.

class Homeview(ListView):
    model=Post
    template_name='home.html'
    context_object_name='post'

