from django.db import models


class AbstractDateTime(models.Model):
    """AbstractDateTime model definition."""

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class AbstractItem(AbstractDateTime):
    """AbstractItem model definition."""

    name = models.CharField(max_length=80)

    class Meta:
        abstract = True

    def __str__(self):
        return self.name
