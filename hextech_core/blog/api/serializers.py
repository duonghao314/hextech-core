from rest_framework import serializers

from hextech_core.blog.models import Blog, BlogCategory
from hextech_core.core.restful.recursive_serializer import RecursiveField


class BlogCategorySerializer(serializers.ModelSerializer):
    child_categories = RecursiveField(many=True)

    class Meta:
        model = BlogCategory
        fields = [
            "id",
            "name",
            "slug",
            "created_at",
            "updated_at",
            "metadata",
            "child_categories",
        ]


class BlogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Blog
        fields = "__all__"
