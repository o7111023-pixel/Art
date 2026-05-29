from django.urls import path
from .views import (
    IndexView,
    ArtistListView,
    PaintingListView,
    GenreListView,
    ArtistCreateView,
    ArtistDetailView,
    PaintingCreateView,
    PaintingDetailView,
    PaintingUpdateView,
    GenreCreateView,
    GenreUpdateView,
    GenreDeleteView,
    ArtistUpdateView,
    ArtistDeleteView,
    PaintingDeleteView,
    ToggleFavoritePaintingView,
    GenreDetailView,
    InterCollectionView,
)

app_name = "museum"

urlpatterns = [
    path("", IndexView.as_view(), name="index"),

    path("artists/", ArtistListView.as_view(), name="artists"),
    path("artists/create/", ArtistCreateView.as_view(), name="artist-create"),
    path("artists/<int:pk>/", ArtistDetailView.as_view(), name="artist-detail"),
    path("artists/<int:pk>/update/", ArtistUpdateView.as_view(), name="artist-update"),
    path("artists/<int:pk>/delete/", ArtistDeleteView.as_view(), name="artist-delete"),

    path("paintings/", PaintingListView.as_view(), name="paintings"),
    path("paintings/create/", PaintingCreateView.as_view(), name="painting-create"),
    path("paintings/<int:pk>/", PaintingDetailView.as_view(), name="painting-detail"),
    path("paintings/<int:pk>/update/", PaintingUpdateView.as_view(), name="painting-update"),
    path("paintings/<int:pk>/delete/", PaintingDeleteView.as_view(), name="painting-delete"),

    path("genres/", GenreListView.as_view(), name="genres"),
    path("genres/create/", GenreCreateView.as_view(), name="genre-create"),
    path("genres/<int:pk>/", GenreDetailView.as_view(), name="genre-detail"),
    path("genres/<int:pk>/update/", GenreUpdateView.as_view(), name="genre-update"),
    path("genres/<int:pk>/delete/", GenreDeleteView.as_view(), name="genre-delete"),

    path(
    "paintings/<int:pk>/toggle-favorite/", ToggleFavoritePaintingView.as_view(),
        name="toggle-favorite-painting"),
    path("intercollection/", InterCollectionView.as_view(), name="intercollection"),
]
