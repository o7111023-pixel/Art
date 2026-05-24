from django.db import models
from django.urls import reverse


class Genre(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        ordering = ("name",)

    def __str__(self):
        return self.name


class Artist(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)

    birth_year = models.IntegerField()
    death_year = models.IntegerField(
        null=True,
        blank=True
    )

    country = models.CharField(max_length=100)

    class Meta:
        ordering = ("last_name",)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Painting(models.Model):
    title = models.CharField(max_length=100)

    description = models.TextField(blank=True)

    year = models.IntegerField()

    price = models.DecimalField(
        max_digits=10,
        decimal_places=2
    )

    genre = models.ForeignKey(
        Genre,
        on_delete=models.CASCADE,
        related_name="paintings"
    )

    artist = models.ForeignKey(
        Artist,
        on_delete=models.CASCADE,
        related_name="paintings"
    )

    class Meta:
        ordering = ("title",)

    def __str__(self):
        return f"{self.title} ({self.year})"

    def get_absolute_url(self):
        return reverse(
            "museum:painting-detail",
            args=[str(self.id)]
        )
