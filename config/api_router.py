from django.conf import settings
from rest_framework.routers import DefaultRouter, SimpleRouter

from hextech_core.blog.api.views import BlogCategoryViewSet, BlogViewSet
from hextech_core.users.api.views import UserViewSet

if settings.DEBUG:
    router = DefaultRouter()
else:
    router = SimpleRouter()


router.register("users", UserViewSet, basename="users")
router.register("blogs/category", BlogCategoryViewSet, basename="blogs-category")
router.register("blogs/blog", BlogViewSet, basename="blogs-blog")

app_name = "api"
urlpatterns = router.urls
