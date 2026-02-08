from django.urls import path
from .views import BlogListCreateApi, BlogDetailApi

urlpatterns = [
    path('', BlogListCreateApi.as_view(), name='blog-list-create'),
    path('<int:blog_id>/', BlogDetailApi.as_view(), name='blog-detail')
]