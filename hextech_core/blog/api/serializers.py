from rest_framework import serializers

from hextech_core.blog.models import BlogCategory


class SubCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = BlogCategory
        fields = "__all__"


class BlogCategorySerializer(serializers.ModelSerializer):
    children = SubCategorySerializer(source="child_categories", many=True)

    class Meta:
        model = BlogCategory
        fields = "__all__"
