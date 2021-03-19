from django.db import models


class BaseModel(models.Model):
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)
    metadata = models.JSONField(blank=True, default=dict)

    class Meta:
        abstract = True

    def update_metadata(self, key, value):
        self.metadata[key] = value
        self.save(update_fields=["metadata"])
