# Django
from django.contrib.auth.models import User
from django.db import models

# First party
from abstracts.models import AbsctractDateTime


class Country(models.Model):
    title = models.CharField(
        verbose_name='название',
        max_length=50
    )

    class Meta:
        verbose_name = 'страна'
        verbose_name_plural = 'страны'

    def __str__(self):
        return self.title


class Band(AbsctractDateTime):
    title = models.CharField(
        verbose_name='название',
        max_length=50
    )
    followers = models.PositiveIntegerField(
        verbose_name='фоловеры',
        default=0
    )
    country = models.OneToOneField(
        to=Country,
        on_delete=models.PROTECT,
        verbose_name='страна'
    )

    class Meta:
        ordering = ('id',)
        verbose_name = 'группа'
        verbose_name_plural = 'группы'

    def __str__(self) -> str:
        if not self.title:
            return 'Без названия'
        return f'Группа: {self.title}'


class Artist(AbsctractDateTime):
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
    band = models.ForeignKey(
        to=Band,
        on_delete=models.PROTECT,
        verbose_name='группа',
        null=True,
        blank=True
    )
    user = models.OneToOneField(
        to=User,
        on_delete=models.PROTECT,
        verbose_name='пользователь',
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
            return 'Без имени'

        return f'Музыкант: {self.nickname}'


class Album(models.Model):
    """
    Album model.
    """
    REGULAR = 0
    SILVER = 1
    GOLD = 2
    PLATINUM = 3
    STATUSES = (
        (REGULAR, 'Обычный'),
        (SILVER, 'Серебряный'),
        (GOLD , 'Золотой'),
        (PLATINUM , 'Платиновый'),
    )
    band = models.ForeignKey(
        to=Band,
        on_delete=models.PROTECT,
        verbose_name='группа'
    )
    title = models.CharField(
        verbose_name='название альбома',
        max_length=150
    )
    release_date = models.DateTimeField(
        verbose_name='дата релиза',
    )
    logo = models.ImageField(
        verbose_name='логотип',
        upload_to='images/',
        null=True,
        blank=True
    )
    status = models.SmallIntegerField(
        choices=STATUSES,
        default=REGULAR,
        verbose_name='статус'
    )

    def __str__(self) -> str:
        return f'{self.band}: {self.title} ({self.status})'

    class Meta:
        ordering = ('release_date',)
        verbose_name = 'альбом'
        verbose_name_plural = 'альбомы'
