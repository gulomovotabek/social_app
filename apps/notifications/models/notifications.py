from django.db import models

from common.models import BaseModel


class NotificationTypes(models.TextChoices):
    LIKE = ("like", "Like")


class Notification(BaseModel):
    type = models.CharField(choices=NotificationTypes.choices, max_length=50)
    post = models.ForeignKey("posts.Post", models.CASCADE, related_name="notifications")
    action_by = models.ForeignKey("users.User", models.CASCADE, related_name="action_notifications")

    class Meta:
        db_table = 'notifications'
        ordering = ['-created_time']
