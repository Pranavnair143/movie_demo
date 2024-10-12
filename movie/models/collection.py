import uuid

from django.db import models
from django.contrib.postgres.fields import ArrayField
from django.contrib.auth import get_user_model

User = get_user_model()

class Collection(models.Model):
    uuid = models.UUIDField(default=uuid.uuid4, editable=False, unique=True, primary_key=True)
    title = models.CharField(max_length=255)
    description = models.TextField()
    movies = ArrayField(
        models.JSONField(),
        blank=True,
        default=list
    )
    user = models.ForeignKey(
        User,
        related_name='user',
        on_delete=models.CASCADE,
        verbose_name="User",
        null=False,
        blank=False
    )

    def __str__(self):
        return self.title
