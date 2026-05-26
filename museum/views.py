from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponseRedirect
from django.views import generic
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from .models import Artist, Painting, Genre


@login_required
def index(request):
    """View function for the home page."""

    num_artists = Artist.objects.count()
    num_paintings = Painting.objects.count()
    num_genres = Genre.objects.count()

    num_visits = request.session.get("num_visits", 0)
    request.session["num_visits"] = num_visits + 1

    artists = Artist.objects.all()
    paintings = Painting.objects.all()
    genres = Genre.objects.all()

    context = {
        "num_artists": num_artists,
        "num_paintings": num_paintings,
        "num_genres": num_genres,
        "num_visits": num_visits + 1,

        "artists": artists,
        "paintings": paintings,
        "genres": genres,
    }

    return render(request, "museum/index.html", context=context)


class ArtistListView(LoginRequiredMixin, generic.ListView):
    model = Artist
    paginate_by = 5
    template_name = "museum/artist_list.html"
    context_object_name = "artist_list"


class ArtistDetailView(LoginRequiredMixin, generic.DetailView):
    model = Artist
    template_name = "museum/artist_detail.html"


class ArtistCreateView(LoginRequiredMixin, generic.CreateView):
    model = Artist
    fields = "__all__"
    success_url = reverse_lazy("museum:artists")


class ArtistUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Artist
    fields = ["username", "first_name", "last_name", "birth_year", "country"]
    success_url = reverse_lazy("museum:artists")


class ArtistDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Artist
    success_url = reverse_lazy("museum:artists")


class PaintingListView(LoginRequiredMixin, generic.ListView):
    model = Painting
    paginate_by = 5
    template_name = "museum/painting_list.html"
    context_object_name = "painting_list"


class PaintingDetailView(LoginRequiredMixin, generic.DetailView):
    model = Painting
    template_name = "museum/painting_detail.html"


class PaintingCreateView(LoginRequiredMixin, generic.CreateView):
    model = Painting
    fields = "__all__"
    success_url = reverse_lazy("museum:paintings")


class PaintingUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Painting
    fields = "__all__"
    template_name = "museum/painting_form.html"
    success_url = reverse_lazy("museum:paintings")


class PaintingDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Painting
    success_url = reverse_lazy("museum:paintings")


class GenreListView(LoginRequiredMixin, generic.ListView):
    model = Genre
    paginate_by = 3
    template_name = "museum/genre_list.html"
    context_object_name = "genre_list"


class GenreCreateView(LoginRequiredMixin, generic.CreateView):
    model = Genre
    fields = "__all__"
    success_url = reverse_lazy("museum:genres")


class GenreUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Genre
    fields = "__all__"
    success_url = reverse_lazy("museum:genres")


class GenreDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Genre
    success_url = reverse_lazy("museum:genres")


class GenreDetailView(LoginRequiredMixin, generic.DetailView):
    model = Genre
    template_name = "museum/genre_detail.html"


class InterCollectionView(LoginRequiredMixin, generic.ListView):
    model = Painting
    template_name = "museum/intercollection.html"
    context_object_name = "items"


@login_required
def toggle_favorite_painting(request, pk):
    artist = Artist.objects.get(id=request.user.id)
    painting = Painting.objects.get(id=pk)

    if painting in artist.favorite_paintings.all():
        artist.favorite_paintings.remove(painting)
    else:
        artist.favorite_paintings.add(painting)

    return HttpResponseRedirect(
        reverse_lazy("museum:painting-detail", args=[pk])
    )
