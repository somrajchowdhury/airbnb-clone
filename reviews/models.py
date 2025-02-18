from django.db import models
from core.models import AbstractDateTime
from rooms.models import Room
from users.models import User


class Review(AbstractDateTime):
    """Review model definition."""

    review = models.TextField()
    cleanliness = models.PositiveSmallIntegerField()
    accuracy = models.PositiveSmallIntegerField()
    check_in = models.PositiveSmallIntegerField()
    communication = models.PositiveSmallIntegerField()
    location = models.PositiveSmallIntegerField()
    value = models.PositiveSmallIntegerField()
    user = models.ForeignKey(to=User, on_delete=models.CASCADE)
    room = models.ForeignKey(to=Room, on_delete=models.CASCADE)


    def __str__(self):
        return f"{self.review} - {self.room}"
