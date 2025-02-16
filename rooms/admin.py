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