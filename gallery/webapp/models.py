from django.contrib.auth.models import User
from django.db import models


class Album(models.Model):
    name = models.CharField(max_length=100, null=True, blank=True, verbose_name='Название')
    description = models.TextField(max_length=2000, null=True, blank=True, verbose_name='Описание')
    author = models.ForeignKey(User, related_name='albums', on_delete=models.CASCADE, verbose_name='Автор')
    create_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    is_private = models.BooleanField(verbose_name='приватный', default=False)

    def __str__(self):
        return self.name


class Photo(models.Model):
    album = models.ForeignKey('webapp.Album', related_name='photos', null=True, blank=True, on_delete=models.CASCADE,
                              verbose_name='Альбом')
    photo = models.ImageField(upload_to='photos', verbose_name='Фото')
    note = models.CharField(max_length=100, verbose_name='Подпись')
    create_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    author = models.ForeignKey(User, related_name='photos', on_delete=models.CASCADE, verbose_name='Автор')
    likes = models.IntegerField(default=0, verbose_name='Лайки')
    is_private = models.BooleanField(verbose_name='приватный', default=False)

    def __str__(self):
        return self.note


class Like(models.Model):
    author = models.ForeignKey(User, related_name='user_likes', on_delete=models.CASCADE, verbose_name='Автор')
    photo = models.ForeignKey('webapp.Photo', related_name='photo_likes', on_delete=models.CASCADE, verbose_name='Фото')

    class Meta:
        unique_together = ('author', 'photo')


class Comment(models.Model):
    text = models.TextField(max_length=500, verbose_name='Текст')
    photo = models.ForeignKey('webapp.Photo', related_name='photo_comments', on_delete=models.CASCADE,
                              verbose_name='Фото')
    author = models.ForeignKey(User, related_name='author_comments', on_delete=models.CASCADE, verbose_name='Автор')
    create_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')

    def __str__(self):
        return self.text
