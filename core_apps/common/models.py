import uuid

from django.db import models
from django.utils import timezone


class TimeStampedModel(models.Model):
    pkid = models.BigAutoField(primary_key=True, editable=False)
    id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True
        ordering = ["-created_at", "-updated_at"]

    def save(self, *args, **kwargs):
        """
         Check if any field in the model has changed
        """
        if self.pk is not None:
            original = self.__class__.objects.get(pk=self.pk)
            if self._has_changed(original):
                self.updated_at = timezone.now()
        
        super().save(*args, **kwargs)

    def _has_changed(self, original):
        """
         Check if any field has changed
        """
        for field in self._meta.fields:
            if getattr(self, field.name) != getattr(original, field.name):
                return True
        return False