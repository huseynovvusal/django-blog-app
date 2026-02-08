from django.utils.text import slugify
from django.db import transaction
from .models import Blog
from typing import TYPE_CHECKING
import uuid

if TYPE_CHECKING:
    from apps.users.models import User

def create_blog(user: "User", title: str, content: str) -> Blog:
    slug = slugify(title)

    if(Blog.objects.filter(slug=slug).exists()):
        slug = f"{slug}-{uuid.uuid4().hex[:8]}"

    with transaction.atomic():
        blog = Blog.objects.create(
            author = user,
            title = title,
            slug = slug,
            content = content
        )

    return blog



