# Generated by Django 3.2 on 2024-05-02 15:24

import django.contrib.auth.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0009_alter_yamdbuser_confirmation_code'),
    ]

    operations = [
        migrations.AlterField(
            model_name='yamdbuser',
            name='email',
            field=models.EmailField(error_messages={'unique': 'Пользователь с такой электронной почтой уже существует!'}, max_length=254, unique=True, verbose_name='Электронная почта'),
        ),
        migrations.AlterField(
            model_name='yamdbuser',
            name='role',
            field=models.CharField(choices=[('user', 'пользователь'), ('moderator', 'модератор'), ('admin', 'администратор')], default='user', max_length=9, verbose_name='Роль пользователя'),
        ),
        migrations.AlterField(
            model_name='yamdbuser',
            name='username',
            field=models.CharField(error_messages={'unique': 'Пользователь с таким именем уже существует!'}, max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='Имя пользователя'),
        ),
    ]
