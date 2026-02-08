from django.urls import path
from .web_views import BlogListView, BlogDetailView

app_name = 'blog_web'

urlpatterns = [
    path('', BlogListView.as_view(), name='list'),
    path('post/<slug:slug>/', BlogDetailView.as_view(), name='detail'),
]
