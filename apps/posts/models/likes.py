from django.db import models

from common.models import BaseModel


class Like(BaseModel):
    action_by = models.ForeignKey("users.User", models.CASCADE, related_name="liked_by")
    post = models.ForeignKey("posts.Post", models.CASCADE, related_name="likes")

    class Meta:
        db_table = "likes"
        ordering = ("-created_time",)
        unique_together = ("post", "action_by")
