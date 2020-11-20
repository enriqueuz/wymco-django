''' Blog URLs. '''

# Django
from django.urls import path

# Views
from . import views

urlpatterns = [
    path('', views.PostList.as_view(), name='blog-home'),
    path('<slug:slug>/', views.PostDetail.as_view(), name='post-detail'),
]