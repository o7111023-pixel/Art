from django.views import generic, View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.views.generic import TemplateView

from museum.models import Artist, Painting, Genre


class IndexView(LoginRequiredMixin, TemplateView):
    template_name = "museum/index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        num_visits = self.request.session.get("num_visits", 0)
        self.request.session["num_visits"] = num_visits + 1

        context["num_artists"] = Artist.objects.count()
        context["num_paintings"] = Painting.objects.count()
        context["num_genres"] = Genre.objects.count()
        context["num_visits"] = num_visits + 1

        context["artists"] = Artist.objects.all()
        context["paintings"] = Painting.objects.all()
        context["genres"] = Genre.objects.all()

        return context


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


class ToggleFavoritePaintingView(LoginRequiredMixin, View):
    def post(self, request, pk):
        artist = Artist.objects.get(id=request.user.id)
        painting = Painting.objects.get(id=pk)

        if painting in artist.favorite_paintings.all():
            artist.favorite_paintings.remove(painting)
        else:
            artist.favorite_paintings.add(painting)

        return HttpResponseRedirect(
            reverse_lazy("museum:painting-detail", args=[pk])
        )
