from django.urls import path
from .views import BlogListCreateApi

urlpatterns = [
    path('', BlogListCreateApi.as_view(), name='blog-list-create')
]