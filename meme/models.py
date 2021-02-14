from django.db import models


class Meme(models.Model):
    name = models.CharField(max_length=50)
    url = models.URLField(blank=True)
    caption = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
