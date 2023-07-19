# Python
from typing import Any

# Django
from django.contrib.auth.models import User
from django.db.models.query import QuerySet
from django.http import HttpResponse
from django.shortcuts import render

# Local
from .models import (
    Album,
    Artist
)


def index(request):
    artists: QuerySet[Artist] = Artist.objects.all()
    albums: QuerySet[Album] = Album.objects.all()

    context: dict[str, QuerySet[Any]] = {
        'artists': artists,
        'albums': albums
    }
    return render(
        request,
        'main/index.html',
        context
    )


def detail(request, album_id):
    user: User = request.user
    album: Album = Album.objects.get(
        id=album_id
    )
    return render(
        request,
        'main/detail.html',
        {
            'album': album,
            'user': user
        }
    )
