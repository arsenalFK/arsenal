# Generated by Django 3.0.5 on 2020-05-13 13:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainn', '0015_auto_20200513_1608'),
    ]

    operations = [
        migrations.AlterField(
            model_name='player',
            name='player_position',
            field=models.CharField(choices=[('Вратарь', 'Вратарь'), ('Защитник', 'Защитник'), ('Полунападение', 'Полунападающий'), ('Полузащита', 'Полузащитник'), ('Нападающий', 'Нападающий'), ('Замена', 'На замене')], default='Замена', help_text='Позиция', max_length=13, verbose_name='Игровая позиция'),
        ),
    ]
