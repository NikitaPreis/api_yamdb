# Generated by Django 3.2 on 2024-04-30 15:08

import django.contrib.auth.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0006_alter_yamdbuser_confirmation_code'),
    ]

    operations = [
        migrations.AlterField(
            model_name='yamdbuser',
            name='confirmation_code',
            field=models.CharField(default=9672, max_length=16, verbose_name='Код подтверждения'),
        ),
        migrations.AlterField(
            model_name='yamdbuser',
            name='email',
            field=models.EmailField(error_messages={'unique': 'Пользователь с таким почтовым адресом уже существует.'}, max_length=254, unique=True, verbose_name='Почтовый адрес'),
        ),
        migrations.AlterField(
            model_name='yamdbuser',
            name='username',
            field=models.CharField(error_messages={'unique': 'Пользователь с таким именем уже существует.'}, max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='Имя пользователя'),
        ),
    ]
