''' Blog views '''

# Django
from django.shortcuts import render
from django.views.generic import ListView, DetailView

# Models
from blog.models import BlogPost

class PostList(ListView):
    ''' Return all pulblished posts. '''
    queryset = BlogPost.objects.filter(status=1).order_by('-created_on')

class PostDetail(DetailView):
    ''' Return post detail. '''
    model = BlogPost
