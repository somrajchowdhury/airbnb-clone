from django.contrib import admin
from . import models


@admin.register(models.Room)
class RoomAdmin(admin.ModelAdmin):
    """Admin class for Room model."""

    pass


@admin.register(models.RoomType)
class RoomTypeAdmin(admin.ModelAdmin):
    """Admin class for RoomType model."""

    pass


@admin.register(models.Amenity)
class AmenityAdmin(admin.ModelAdmin):
    """Admin class for Amenity model."""

    pass


@admin.register(models.Facility)
class FacilityAdmin(admin.ModelAdmin):
    """Admin class for Facility model."""

    pass


@admin.register(models.HouseRule)
class HouseRuleAdmin(admin.ModelAdmin):
    """Admin class for HouseRule model."""

    pass


@admin.register(models.Photo)
class PhotoAdmin(admin.ModelAdmin):
    """Admin class for Photo model."""

    pass
