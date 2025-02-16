from django.db import models
from django_countries.fields import CountryField
from core.models import AbstractDateTime, AbstractItem
from users.models import User


class RoomType(AbstractItem):
    """RoomType model definition."""

    pass


class Room(AbstractDateTime):
    """Room model definition."""

    name = models.CharField(max_length=140)
    description = models.TextField()
    host = models.ForeignKey(to=User, on_delete=models.CASCADE)
    country = CountryField()
    city = models.CharField(max_length=80)
    price = models.IntegerField()
    address = models.CharField(max_length=140)
    guests = models.IntegerField()
    beds = models.IntegerField()
    bedrooms = models.IntegerField()
    baths = models.IntegerField()
    check_in = models.TimeField()
    check_out = models.TimeField()
    instant_book = models.BooleanField(default=False)
    room_type = models.ManyToManyField(to=RoomType, blank=True)

    def __str__(self):
        return self.name
