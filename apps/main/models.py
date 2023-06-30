# Django
from django.contrib.auth.models import User
from django.db import models


class Artist(models.Model):
    """
    Artist model.
    """
    GENDER_OTHER = 0
    GENDER_FEMALE = 1
    GENDER_MALE = 2
    GENDERS = (
        (GENDER_OTHER, 'Остальное'),
        (GENDER_FEMALE, 'Женщина'),
        (GENDER_MALE, 'Мужчина')
    )
    user = models.OneToOneField(
        to=User,
        on_delete=models.PROTECT,
        verbose_name='исполнитель',
        null=True,
        blank=True
    )
    nickname = models.CharField(
        verbose_name='псевдоним',
        default='',
        max_length=50
    )
    gender = models.PositiveSmallIntegerField(
        choices=GENDERS,
        verbose_name='гендер',
        default=GENDER_OTHER
    )

    class Meta:
        ordering = ('id',)
        verbose_name = 'музыкант'
        verbose_name_plural = 'музыканты'

    def __str__(self) -> str:
        if not self.nickname:
            return 'Noname'

        return f'Artist: {self.nickname}'


class Band(models.Model):
    """
    Band model.
    """
    pass
