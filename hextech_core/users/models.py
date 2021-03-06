from django.contrib.auth.models import AbstractUser
from django.db.models import BigIntegerField, CharField
from django.urls import reverse
from django.utils.translation import gettext_lazy as _

from hextech_core.core.utils.id import RandomID


class User(AbstractUser):
    """Default user for Hextech Core Project."""

    #: First and last name do not cover name patterns around the globe
    # name = CharField(_("Name of User"), blank=True, max_length=255)
    id = BigIntegerField(
        _("Random id"), default=RandomID("users.User"), primary_key=True
    )
    first_name = CharField(_("First name of User"), blank=True, max_length=20)  # type: ignore
    last_name = CharField(_("Last name of User"), blank=True, max_length=20)  # type: ignore

    def get_absolute_url(self):
        """Get url for user's detail view.

        Returns:
            str: URL for user detail.

        """
        return reverse("users:detail", kwargs={"username": self.username})
