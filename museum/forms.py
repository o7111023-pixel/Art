from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError

from museum.models import Artist, Painting


class ArtistCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = Artist
        fields = (
            "username",
            "first_name",
            "last_name",
            "birth_year",
            "country",
        )

    def clean_birth_year(self):
        birth_year = self.cleaned_data.get("birth_year")

        if birth_year is not None:
            if birth_year < 1000 or birth_year > 2026:
                raise ValidationError("Enter a valid birth year (1000–2026)")

        return birth_year


class PaintingForm(forms.ModelForm):
    class Meta:
        model = Painting
        fields = "__all__"


class PaintingSearchForm(forms.Form):
    title = forms.CharField(
        max_length=100,
        required=False,
        label="",
        widget=forms.TextInput(attrs={
            "placeholder": "Search painting title"
        }),
    )
