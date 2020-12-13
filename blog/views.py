''' Blog views '''
from datetime import date, timedelta
# Django
from django.shortcuts import render
from django.views.generic import ListView, DetailView

# Models
from blog.models import BlogPost

class BlogPostsSidebarMixin(object):
    ''' Return recently published posts for sidebar '''
    def get_context_data(self, **kwargs):
        # Return latest post for sidebar
        today = date.today()
        context = super().get_context_data(**kwargs)
        context['blogpost_list_sidebar_news'] = BlogPost.objects.filter(status=1, created_on__gte=today-timedelta(days=3)).order_by('-created_on')
        context['blogpost_list_sidebar'] = BlogPost.objects.filter(status=1, created_on__lte=today-timedelta(days=3)).order_by('-created_on')[:3]
        return context

class PostList(BlogPostsSidebarMixin, ListView):
    ''' Return all published posts. '''
    queryset = BlogPost.objects.filter(status=1).order_by('-created_on')
    paginate_by = 5

class PostDetail(BlogPostsSidebarMixin, DetailView):
    ''' Return post detail. '''
    model = BlogPost
