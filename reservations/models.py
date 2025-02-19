from django.db import models
from core.models import AbstractDateTime
from rooms.models import Room
from users.models import User


class Reservation(AbstractDateTime):
    """Reservation model definition."""

    STATUS_PENDING = "pending"
    STATUS_CONFIRMED = "confirmed"
    STATUS_CANCELED = "canceled"

    STATUS_CHOICES = (
        (STATUS_PENDING, "Pending"),
        (STATUS_CONFIRMED, "Confirmed"),
        (STATUS_CANCELED, "Canceled")
    )

    status = models.CharField(max_length=20, choices=STATUS_CHOICES,
                              default=STATUS_PENDING)
    check_in = models.DateField()
    check_out = models.DateField()
    guest = models.ForeignKey(to=User, on_delete=models.CASCADE)
    room = models.ForeignKey(to=Room, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.room} - {self.check_in}"
