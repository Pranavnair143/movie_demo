from django.db import models


class AppSettings(models.Model):
    request_count = models.IntegerField(default=0, null=False, blank=False)

    def __str__(self):
        return "App Setting"
