from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class UsersConfig(AppConfig):
    name = "hextech_core.users"
    verbose_name = _("Users")

    def ready(self):
        try:
            import hextech_core.users.signals  # noqa F401
        except ImportError:
            pass
