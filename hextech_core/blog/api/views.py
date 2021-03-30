from hextech_core.blog.api.serializers import BlogCategorySerializer
from hextech_core.blog.models import BlogCategory
from hextech_core.core.restful.base_views import BaseViewSet


class BlogCategoryViewSet(BaseViewSet):
    serializer_class = BlogCategorySerializer

    def get_queryset(self):
        return BlogCategory.objects.filter(parent__isnull=True)
