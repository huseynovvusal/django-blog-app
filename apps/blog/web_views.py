from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, DetailView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from .services import create_blog
from .selectors import blog_list
from .models import Blog

class BlogListView(ListView):
    model = Blog
    template_name = 'blog/list.html'
    context_object_name = 'blogs'
    paginate_by = 10

    def get_queryset(self):
        return blog_list()

class BlogCreateView(LoginRequiredMixin, CreateView):
    template_name = 'blog/create.html'
    model = Blog # Standard View needs model usually, but we override post anyway for service
    fields = ['title', 'content'] # Not used since template has manual form, but required by CreateView if no form_class
    
    def post(self, request, *args, **kwargs):
        title = request.POST.get('title')
        content = request.POST.get('content')
        
        if title and content:
            try:
                # Use our Service Layer!
                create_blog(user=request.user, title=title, content=content)
                return redirect('blog_web:list')
            except Exception as e:
                # Handle potential duplicate slugs or database errors
                return render(request, self.template_name, {'error': str(e)})
            
        return render(request, self.template_name, {'error': 'Title and Content required.'})

class BlogDetailView(DetailView):
    model = Blog
    template_name = 'blog/detail.html'
    context_object_name = 'blog'
    slug_field = 'slug'
    slug_url_kwarg = 'slug'
