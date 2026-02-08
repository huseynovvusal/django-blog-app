from django.db.models import QuerySet
from .models import Blog

def blog_list() -> QuerySet[Blog]:
    return Blog.objects.select_related("author").all()

