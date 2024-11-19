from django.db import models

from common.models import BaseModel


class Post(BaseModel):
    author = models.ForeignKey("users.User", models.CASCADE, related_name="posts")
    content = models.URLField()

    class Meta:
        db_table = 'posts'
        ordering = ['-created_time']
