# Generated by Django 3.2 on 2024-05-02 13:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0008_auto_20240430_1810'),
    ]

    operations = [
        migrations.AlterField(
            model_name='yamdbuser',
            name='confirmation_code',
            field=models.CharField(blank=True, max_length=5, verbose_name='Код подтверждения'),
        ),
    ]
