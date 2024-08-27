from django.contrib.auth import get_user_model
from django.db import models

from core import constants as const

User = get_user_model()


class NameSlugBaseModel(models.Model):
    name = models.CharField(max_length=const.MAX_LENGTH_NAME_FIELD,
                            verbose_name='Название')
    slug = models.SlugField(unique=True,
                            verbose_name='Слаг')

    class Meta:
        abstract = True
        ordering = ('name',)
        default_permissions = (
            'add', 'delete', 'view'
        )

    def __str__(self):
        return self.name


class ReviewCommentBaseModel(models.Model):
    text = models.TextField(verbose_name='Текст')
    pub_date = models.DateTimeField(
        auto_now_add=True, verbose_name='Дата публикации'
    )
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        verbose_name='Автор')

    class Meta:
        abstract = True
        ordering = ('-pub_date', 'text')

    def __str__(self):
        return self.text
