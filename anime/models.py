from django.db import models
from django.contrib.auth.models import User


class WatchListItem(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="watchlist")
    title = models.CharField(max_length=255)
    watched = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.title} ({'watched' if self.watched else 'not watched'})"

