from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    """
    Abstract user model has name field. I used first_name and last_name for name field
    """
    avatar = models.ImageField(upload_to="avatars/", null=True, blank=True)

    class Meta:
        db_table = 'users'
        ordering = ['-date_joined']
