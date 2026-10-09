from django.db import models

from .constants import DEFAULT_GREETING


class Greeting(models.Model):
    message = models.CharField(max_length=200, default=DEFAULT_GREETING)
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.message
