from django.db import models
from core.models import AbstractDateTime
from users.models import User
from rooms.models import Room


class List(AbstractDateTime):
    """List model definition."""

    name = models.CharField(max_length=80)
    user = models.ForeignKey(to=User, on_delete=models.CASCADE)
    room = models.ManyToManyField(to=Room, blank=True)

    def __str__(self):
        return self.name
