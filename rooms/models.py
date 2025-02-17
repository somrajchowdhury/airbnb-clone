from django.db import models
from django_countries.fields import CountryField
from core.models import AbstractDateTime, AbstractItem
from users.models import User


class RoomType(AbstractItem):
    """RoomType model definition."""

    class Meta:
        verbose_name = 'Room Type'


class Amenity(AbstractItem):
    """Amenity model definition."""

    class Meta:
        verbose_name_plural = 'Amenities'


class Facility(AbstractItem):
    """Facility model definition."""

    class Meta:
        verbose_name_plural = 'Facilities'


class HouseRule(AbstractItem):
    """HouseRule model definition."""

    class Meta:
        verbose_name = 'House Rule'


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
    room_type = models.ForeignKey(to=RoomType, on_delete=models.SET_NULL,
                                  null=True)
    amenities = models.ManyToManyField(to=Amenity, blank=True)
    facilities = models.ManyToManyField(to=Facility, blank=True)
    house_rules = models.ManyToManyField(to=HouseRule, blank=True)

    def __str__(self):
        return self.name


class Photo(AbstractDateTime):
    """Photo model definition."""

    caption = models.CharField(max_length=80)
    file = models.ImageField()
    room = models.ForeignKey(to=Room, on_delete=models.CASCADE)

    def __str__(self):
        return self.caption
