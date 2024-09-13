import uuid
from django.db import models
from accounts.models import User

class Recipe(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    preparation = models.TextField()
    ingredients = models.TextField()
    unique_token = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name="recipes")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.title
