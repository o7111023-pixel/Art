from django.contrib.auth.models import AbstractUser
from django.db import models


class Genre(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        ordering = ("name",)

    def __str__(self):
        return self.name


class Artist(AbstractUser):
    birth_year = models.PositiveIntegerField(null=True, blank=True)
    country = models.CharField(max_length=100, null=True, blank=True)

    favorite_paintings = models.ManyToManyField(
        "Painting",
        blank=True,
        related_name="liked_by"
    )

    class Meta:
        ordering = ("username",)

    def __str__(self):
        return self.username


class Painting(models.Model):
    title = models.CharField(max_length=100)

    price = models.DecimalField(max_digits=10, decimal_places=2)

    year_created = models.PositiveIntegerField(null=True, blank=True)

    description = models.TextField(blank=True)

    artist = models.ForeignKey(
        Artist,
        on_delete=models.CASCADE,
        related_name="paintings"
    )

    genre = models.ForeignKey(
        "Genre",
        on_delete=models.SET_NULL,
        null=True,
        related_name="paintings"
    )

    class Meta:
        ordering = ("title",)

    def __str__(self):
        return self.title
