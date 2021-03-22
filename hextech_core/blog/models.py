from django.db import models
from django.utils import timezone
from django.utils.text import slugify
from wagtail.core.fields import RichTextField

from hextech_core.core.models.base_model import MetadataModel


class BlogCategory(MetadataModel):
    parent = models.ForeignKey(
        "self",
        on_delete=models.PROTECT,
        related_name="child_categories",
        null=True,
        blank=True,
    )
    name = models.CharField(max_length=100)
    slug = models.SlugField(blank=True, unique=True, db_index=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name


class Blog(MetadataModel):
    author = models.ForeignKey(
        "users.User", on_delete=models.CASCADE, related_name="blogs", db_index=True
    )
    category = models.ForeignKey(
        BlogCategory,
        on_delete=models.SET_NULL,
        related_name="blogs",
        db_index=True,
        null=True,
    )
    title = models.CharField(max_length=400)
    content = RichTextField()
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
