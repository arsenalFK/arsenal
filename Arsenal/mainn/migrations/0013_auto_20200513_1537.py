# Generated by Django 3.0.5 on 2020-05-13 12:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainn', '0012_auto_20200511_1344'),
    ]

    operations = [
        migrations.AlterField(
            model_name='player',
            name='player_position',
            field=models.PositiveSmallIntegerField(choices=[('Goalkeeper', 'Вратарь'), (2, 'Защитник'), (3, 'Полузащитник'), (6, 'Полунападающий'), (4, 'Нападающий'), (5, 'На замене')], default=5, help_text='Позиция', verbose_name='Игровая позиция'),
        ),
    ]
