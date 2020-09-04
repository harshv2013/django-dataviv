from django.apps import AppConfig

from camera.models import User

from django.db.models.signals import post_save
from camera.signals import password_reset_token_created


class CameraConfig(AppConfig):
    name = 'camera'
    verbose_name = 'camerax'

    def ready(self):
        import camera.signals
        # post_save.connect(password_reset_token_created, sender=User)
