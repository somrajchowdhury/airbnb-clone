from django.contrib import admin
from . import models


@admin.register(models.Conversation)
class ConversationAdmin(admin.ModelAdmin):
    """Admin class for Conversation model."""

    pass


@admin.register(models.Message)
class MessageAdmin(admin.ModelAdmin):
    """Admin class for Message class."""

    pass
