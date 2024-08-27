# Generated by Django 3.2 on 2024-05-12 05:12

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('reviews', '0015_auto_20240511_1115'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'default_permissions': ('add', 'delete', 'view'), 'ordering': ('name',), 'verbose_name': 'объект «Категория»', 'verbose_name_plural': 'объекты «Категорий»'},
        ),
        migrations.AlterModelOptions(
            name='comment',
            options={'default_related_name': 'comments', 'ordering': ('-pub_date', 'text'), 'verbose_name': 'Комментарий'},
        ),
        migrations.AlterModelOptions(
            name='genre',
            options={'default_permissions': ('add', 'delete', 'view'), 'ordering': ('name',), 'verbose_name': 'объект «Жанр»', 'verbose_name_plural': 'объекты «Жанров»'},
        ),
        migrations.AlterModelOptions(
            name='review',
            options={'default_related_name': 'review', 'ordering': ('-pub_date', 'text'), 'verbose_name': 'Отзыв', 'verbose_name_plural': 'Отзывы'},
        ),
        migrations.AlterModelOptions(
            name='title',
            options={'default_permissions': ('add', 'change', 'delete', 'view'), 'ordering': ('name', '-year'), 'verbose_name': 'объект «Произведение»'},
        ),
        migrations.AlterField(
            model_name='comment',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to=settings.AUTH_USER_MODEL, verbose_name='Пользователь'),
        ),
        migrations.AlterField(
            model_name='review',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='review', to=settings.AUTH_USER_MODEL, verbose_name='Пользователь'),
        ),
    ]
