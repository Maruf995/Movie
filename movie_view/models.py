from django.db import models
from movie import settings


# Create your models here.

class Genre(models.Model):
    title = models.CharField(verbose_name='Жанр', max_length=50)
    url = models.SlugField(max_length=160, unique=True)

    def __str__(self):
        return f'{self.title}'

    class Meta:
        verbose_name = 'Жанр'
        verbose_name_plural = 'Создание Жанров'

class Movie(models.Model):
    image = models.ImageField(verbose_name='Изображение', upload_to='image_movie')
    title = models.CharField(verbose_name='Название', max_length=50)
    tag = models.CharField(verbose_name='Тег', max_length=100)
    genres = models.ManyToManyField(Genre, verbose_name='Жанр')
    year = models.PositiveSmallIntegerField(verbose_name='Дата выхода', default=2023)
    description = models.TextField(verbose_name='Описание', max_length=500)
    favourite = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='post_favourite', blank=True)

    def __str__(self):
        return f'{self.title}'

    class Meta:
        verbose_name = 'Фильмы'
        verbose_name_plural = 'Создание Фильмов'
