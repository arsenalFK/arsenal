# Generated by Django 3.0.5 on 2020-05-01 20:34

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainn', '0005_auto_20200429_1243'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news',
            name='news_likes',
            field=models.IntegerField(default=0, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(99)]),
        ),
    ]
