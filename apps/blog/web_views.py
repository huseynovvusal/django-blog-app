from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView
from .selectors import blog_list
from .models import Blog

class BlogListView(ListView):
    model = Blog
    template_name = 'blog/list.html'
    context_object_name = 'blogs'
    paginate_by = 10  # Built-in ListView pagination

    def get_queryset(self):
        # reuse selector logic but simpler.
        # standard list view calls all() by default.
        # let's use our selector for consistency if filters needed, 
        # but for now standard ORM usage in get_queryset is fine.
        # Wait, selector does select_related.
        return blog_list()

class BlogDetailView(DetailView):
    model = Blog
    template_name = 'blog/detail.html'
    context_object_name = 'blog'
    slug_field = 'slug'
    slug_url_kwarg = 'slug'
