# Generated by Django 3.2 on 2024-04-29 17:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_alter_yamdbuser_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='yamdbuser',
            name='email',
            field=models.EmailField(max_length=254, verbose_name='Почтовый адрес'),
        ),
    ]
