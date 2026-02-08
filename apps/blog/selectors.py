from django.db.models import QuerySet
from .models import Blog

from datetime import datetime

def blog_list(*, filters=None) -> QuerySet[Blog]:
    filters = filters or {}
    
    qs = Blog.objects.select_related("author").all()

    if filters.get("search"):
        qs = qs.filter(title__icontains=filters["search"])
    
    if filters.get("author_id"):
        qs = qs.filter(author_id=filters["author_id"])

    if filters.get("created_at"):
        try:
            date_filter = datetime.strptime(filters['created_at'], '%Y-%m-%d').date()
            qs = qs.filter(created_at__date=date_filter)
        except ValueError:
            pass  # Or raise validation error

    return qs.order_by("-created_at")
