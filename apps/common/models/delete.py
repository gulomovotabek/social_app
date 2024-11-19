from common.queryset import DeleteManager
from django.db import models


class DeleteModel(models.Model):
    is_active = models.BooleanField(default=True)

    objects = DeleteManager()

    class Meta:
        abstract = True

    def delete(self, **kwargs):
        self.is_active = False
        self.save()
