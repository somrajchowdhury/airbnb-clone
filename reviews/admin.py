from django.contrib import admin
from . import models


@admin.register(models.Review)
class ReviewAdmin(admin.ModelAdmin):
    """Admin class for Review model."""

    pass
