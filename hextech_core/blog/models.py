from django.db import models
from django.utils import timezone
from django.utils.text import slugify

from hextech_core.core.models.base_model import BaseModel


class Blog(BaseModel):
    author = models.ForeignKey(
        "users.User", on_delete=models.CASCADE, related_name="blogs", db_index=True
    )
    title = models.CharField(max_length=400)
    content = models.TextField()
    slug = models.SlugField(blank=True, unique=True, db_index=True)
    published = models.BooleanField(default=True)
    published_at = models.DateTimeField(null=True, blank=True)

    class Meta:
        unique_together = ("author", "title")

    def save(self, *args, **kwargs):
        if self.published and not self.published_at:
            self.published_at = timezone.now()
        self.slug = f"{slugify(self.title)}-{self.author.id}"
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title
