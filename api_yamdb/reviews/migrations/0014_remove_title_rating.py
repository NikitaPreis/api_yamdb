# Generated by Django 3.2 on 2024-05-07 11:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0013_rename_reting_title_rating'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='title',
            name='rating',
        ),
    ]
