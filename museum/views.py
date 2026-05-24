from django.http import HttpResponse


def index(request):
    return HttpResponse("Museum Home Page")
