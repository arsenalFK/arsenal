# Generated by Django 3.0.5 on 2020-06-03 10:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainn', '0018_auto_20200603_0149'),
    ]

    operations = [
        migrations.AddField(
            model_name='player',
            name='height',
            field=models.SmallIntegerField(default=0, null=True),
        ),
        migrations.AddField(
            model_name='player',
            name='weight',
            field=models.SmallIntegerField(default=0, null=True),
        ),
    ]