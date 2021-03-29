from rest_framework.viewsets import ModelViewSet

from hextech_core.blog.api.serializers import BlogCategorySerializer
from hextech_core.blog.models import BlogCategory


class BlogCategoryViewSet(ModelViewSet):
    serializer_class = BlogCategorySerializer
    queryset = BlogCategory.objects.all()
