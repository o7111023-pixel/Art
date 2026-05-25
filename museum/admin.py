from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import Artist, Painting, Genre


@admin.register(Artist)
class ArtistAdmin(UserAdmin):
    list_display = UserAdmin.list_display + ("birth_year", "country")
    list_filter = ("country",)
    search_fields = ("username", "first_name", "last_name", "country")

    fieldsets = UserAdmin.fieldsets + (
        ("Additional info", {
            "fields": ("birth_year", "country")
        }),
    )

    add_fieldsets = UserAdmin.add_fieldsets + (
        ("Additional info", {
            "fields": ("first_name", "last_name", "birth_year", "country")
        }),
    )


@admin.register(Painting)
class PaintingAdmin(admin.ModelAdmin):
    list_display = ("title", "artist", "genre", "year_created", "price")
    list_filter = ("genre", "artist", "year_created")
    search_fields = ("title", "artist__username", "genre__name")


@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    list_display = ("name",)
    search_fields = ("name",)
