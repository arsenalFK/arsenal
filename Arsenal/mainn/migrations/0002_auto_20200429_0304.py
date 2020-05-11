# Generated by Django 3.0.5 on 2020-04-29 00:04

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainn', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='player',
            name='player_ATK',
            field=models.SmallIntegerField(help_text='Показатель нападения', validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(99)]),
        ),
        migrations.AlterField(
            model_name='player',
            name='player_DEF',
            field=models.SmallIntegerField(help_text='Показатель защиты', validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(99)]),
        ),
        migrations.AlterField(
            model_name='player',
            name='player_GK',
            field=models.SmallIntegerField(help_text='Показатель голкипера', validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(99)]),
        ),
        migrations.AlterField(
            model_name='player',
            name='player_MID',
            field=models.SmallIntegerField(help_text='Показатель полузащиты', validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(99)]),
        ),
        migrations.AlterField(
            model_name='player',
            name='player_position',
            field=models.PositiveSmallIntegerField(choices=[(1, 'Вратарь'), (1, 'Защитник'), (2, 'Полузащитник'), (3, 'Нападающий'), (4, 'На замене')], default=4, help_text='Позиция'),
        ),
    ]
