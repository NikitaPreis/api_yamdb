# Generated by Django 3.2 on 2024-05-08 12:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0012_remove_yamdbuser_confirmation_code'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='yamdbuser',
            options={'ordering': ['username'], 'verbose_name': 'пользователь', 'verbose_name_plural': 'пользователи'},
        ),
    ]
