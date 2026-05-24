from django.urls import path

from museum.views import index


app_name = "museum"

urlpatterns = [
    path("", index, name="index"),
]
