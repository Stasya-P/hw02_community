from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


class Post(models.Model):
    text = models.TextField(
        verbose_name='Поле для текста')
    pub_date = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Дата публикации')
    author = models.ForeignKey(
        User, on_delete=models.CASCADE,
        related_name='posts',
        verbose_name='Автор публикации')
    group = models.ForeignKey(
        'Group', on_delete=models.SET_NULL,
        blank=True, null=True,
        related_name='posts',
        verbose_name='Сообщество')

    class Meta:
        ordering = ['-pub_date']


class Group(models.Model):
    title = models.CharField(
        max_length=200,
        verbose_name='Название сообщества')
    slug = models.SlugField(
        unique=True,
        verbose_name='Адрес сообщества')
    description = models.TextField(
        verbose_name='Описание сообщества')

    def __str__(self):
        return self.title
