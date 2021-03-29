from django.conf import settings
from rest_framework.routers import DefaultRouter, SimpleRouter

from hextech_core.blog.api.views import BlogCategoryViewSet
from hextech_core.users.api.views import UserViewSet

if settings.DEBUG:
    router = DefaultRouter()
else:
    router = SimpleRouter()


router.register("users", UserViewSet)
router.register("blogs/category", BlogCategoryViewSet)

app_name = "api"
urlpatterns = router.urls
