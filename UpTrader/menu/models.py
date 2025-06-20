from django.db import models
from django.urls import reverse, NoReverseMatch


class Menu(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name


class MenuItem(models.Model):
    menu = models.ForeignKey(
        Menu, related_name="items", on_delete=models.CASCADE
    )
    title = models.CharField(max_length=100)
    parent = models.ForeignKey(
        "self",
        null=True,
        blank=True,
        related_name="children",
        on_delete=models.CASCADE,
    )
    named_url = models.CharField(max_length=100, blank=True)
    url = models.CharField(max_length=200, blank=True)

    def get_absolute_url(self):
        if self.named_url:
            try:
                return reverse(self.named_url)
            except NoReverseMatch:
                return "#"
        return self.url or "#"

    def __str__(self):
        return self.title
