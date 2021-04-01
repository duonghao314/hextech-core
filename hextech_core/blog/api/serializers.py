from rest_framework import serializers

from hextech_core.blog.models import Blog, BlogCategory
from hextech_core.core.restful.recursive_serializer import RecursiveField
from hextech_core.users.api.serializers import UserSerializer


class SmallBlogCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = BlogCategory
        fields = [
            "id",
            "name",
            "slug",
            "metadata",
        ]


class BlogCategorySerializer(SmallBlogCategorySerializer):
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
    author = UserSerializer()
    category = SmallBlogCategorySerializer()

    class Meta:
        model = Blog
        fields = "__all__"
