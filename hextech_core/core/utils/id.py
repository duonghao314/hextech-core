import random

from django.apps import apps
from django.conf import settings
from django.db.utils import OperationalError, ProgrammingError
from django.utils.deconstruct import deconstructible


@deconstructible
class RandomID(object):
    def __init__(self, model_param):
        """:param: model - can be model name as string or model class"""
        self.model_param = model_param

    def __call__(self):
        if isinstance(self.model_param, str):
            model_name = self.model_param
            try:
                model_class = apps.get_model(self.model_param)
            except LookupError:
                model_class = None
        else:
            model_class = self.model_param
            model_name = (
                self.model_param._meta.app_label
                + "."
                + self.model_param._meta.object_name
            )

        random_id_conf: dict = settings.RANDOM_ID.get("default")
        minimum: int = random_id_conf.get("MIN")
        maximum: int = random_id_conf.get("MAX")
        retries: int = 0
        ModelClass = model_class

        while True:
            random_id: int = random.randint(minimum, maximum)
            if model_name is None:
                return random_id
            try:
                ModelClass.objects.get(id=random_id)
            except ModelClass.DoesNotExist:
                break
            except (ProgrammingError, OperationalError):
                return None
            retries += 1
            if retries >= random_id_conf.get("GROW_AFTER_COLLISIONS"):
                maximum = maximum * random_id_conf.get("GROWTH_FACTOR")
                retries = 0
        return random_id
