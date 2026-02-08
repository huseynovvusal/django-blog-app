from django.db import models
from django.conf import settings
from apps.common.models import BaseModel

class Blog(BaseModel):
    objects = models.Manager() 
    
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='blogs'
    )
    
    title = models.CharField(max_length=255)
    slug = models.SlugField(unique=True, max_length=255)
    content = models.TextField()

    def __str__(self):
        return self.title