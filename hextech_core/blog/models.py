from django.db import models
from django.utils import timezone
from django.utils.text import slugify
from django.utils.translation import gettext_lazy as _
from modelcluster.fields import ParentalKey
from modelcluster.models import ClusterableModel
from wagtail.core.fields import RichTextField

from hextech_core.core.models.base_model import BaseModel, MetadataModel
from hextech_core.core.utils import no_accent_vietnamese
from hextech_core.core.utils.id import RandomID
from hextech_core.users.models import User


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


class BlogTag(BaseModel):
    tag = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.tag

    @classmethod
    def tagger(cls, tag: str) -> str:
        tag = no_accent_vietnamese(tag)
        tag = "".join([ele.title() for ele in tag.split(" ")])
        return tag

    def save(self, *args, **kwargs):
        if not self.pk:
            self.tag = self.tagger(self.tag)
        return super().save()


class Blog(ClusterableModel, MetadataModel):
    id = models.BigIntegerField(
        _("Random id"), default=RandomID("blog.Blog"), primary_key=True
    )
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
    slug = models.SlugField(blank=True, unique=True, db_index=True, max_length=450)
    tags = models.ManyToManyField(BlogTag, blank=True)
    published = models.BooleanField(default=True)
    published_at = models.DateTimeField(null=True, blank=True)

    class Meta:
        unique_together = ("author", "title")

    def save(self, *args, **kwargs):
        print(self.__dict__)
        if self.published and not self.published_at:
            self.published_at = timezone.now()
        self.slug = f"{slugify(self.title)}-{self.author.id}"
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title


class BlogComment(BaseModel):
    blog = ParentalKey(Blog, on_delete=models.CASCADE, related_name="comments")
    content = RichTextField()
    title = models.CharField(max_length=255)
    created_by = models.ForeignKey(
        "users.User", on_delete=models.CASCADE, related_name="+", null=True, blank=True
    )

    def __str__(self):
        return f"#{self.blog.id} - {self.title if self.title else 'Untitled'}"


class BlogLike(BaseModel):
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE, related_name="likes")
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="liked")
    is_like = models.BooleanField(default=True)

    class Meta:
        unique_together = ("blog", "user")
