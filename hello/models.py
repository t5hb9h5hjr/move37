from django.db import models


class Greeting(models.Model):
    message = models.CharField(max_length=200, default="Hello, human")
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.message
