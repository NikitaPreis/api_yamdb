# Generated by Django 3.2 on 2024-05-08 09:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0011_alter_yamdbuser_options'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='yamdbuser',
            name='confirmation_code',
        ),
    ]
