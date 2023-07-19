# Third party
import mutagen

# Django
from django.db.models.base import ModelBase
from django.db.models.signals import (
    post_delete,
    post_save,
    pre_delete,
    pre_save
)
from django.dispatch import receiver

# First party
from main.models import Song


@receiver(
    post_save,
    sender=Song
)
def post_save_song(
    sender: ModelBase,
    instance: Song,
    created: bool,
    **kwargs: dict
) -> None:
    """Signal post-save Song."""

    if created:
        # TODO: отправлять письмо юзеру
        #       при добавлении песни
        #
        #       Вы успешно загрузили песню на наш сайт !
        #       ID вашей песни: {song.id}
        #
        mfile: mutagen.File = mutagen.File(
            instance.audio_file
        )
        instance.duration = mfile.info.length
        instance.save()


@receiver(
    pre_save,
    sender=Song
)
def pre_save_anime(
    sender: ModelBase,
    instance: Song,
    **kwargs: dict
) -> None:
    """Signal pre-save Song."""
    pass
