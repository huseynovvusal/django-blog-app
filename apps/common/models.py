import uuid
from django.db import models

class BaseModel(models.Model):
    """
    Abstract base model that provides self-updating
    'created_at' and 'updated_at' fields, plus a UUID.
    """
    uid = models.UUIDField(
        default=uuid.uuid4, 
        editable=False, 
        unique=True,
        db_index=True
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True # This means no table is created for this model

