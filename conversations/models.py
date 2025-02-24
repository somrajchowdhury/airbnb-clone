from django.db import models
from core.models import AbstractDateTime
from users.models import User


class Conversation(AbstractDateTime):
    """Conversation model definition."""

    participants = models.ManyToManyField(to=User, blank=True)

    def __str__(self):
        return f"{self.created}"


class Message(AbstractDateTime):
    """Message model definition."""

    message = models.TextField()
    user = models.ForeignKey(to=User, on_delete=models.CASCADE)
    conversation = models.ForeignKey(to=Conversation,
                                     on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.user} says: {self.message}"
