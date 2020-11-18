''' Blog URLs. '''

# Django
from django.urls import path

# Views
from . import views

urlpatterns = [
    path('', views.blog, name='blog-home')
]