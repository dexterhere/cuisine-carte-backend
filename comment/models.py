import uuid
from django.db import models
from accounts.models import User

class Comment(models.Model):
    unique_token = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="comments")
    comment = models.TextField()
    rating = models.DecimalField(max_digits=2, decimal_places=1, default=0.0)  # Rating between 0.0 to 5.0
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f'Comment by {self.user.name} with rating {self.rating}'
