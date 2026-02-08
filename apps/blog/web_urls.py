from django.urls import path
from .web_views import BlogListView, BlogDetailView, BlogCreateView

app_name = 'blog_web'

urlpatterns = [
    path('', BlogListView.as_view(), name='list'),
    path('write/', BlogCreateView.as_view(), name='create'),
    path('post/<slug:slug>/', BlogDetailView.as_view(), name='detail'),
]
