# Django
from django.http import HttpResponse
from django.shortcuts import render

# Local
from .models import Artist


def index(request):
    artists = Artist.objects.all()
    context = {
        'artists': artists
    }
    return render(
        request,
        'main/index.html',
        context
    )
