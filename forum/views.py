from django.shortcuts import render
from django.views import generic
from .models import Post


class PostList(generic.ListView):
    '''List view for posts'''
    model = Post
    paginate_by = 10
    template_name = 'index.html'
    queryset = Post.objects.all().order_by('-created_on')