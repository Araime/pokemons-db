# Generated by Django 3.1.12 on 2021-06-15 17:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pokemon_entities', '0007_auto_20210615_1954'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pokemon',
            name='element_type',
            field=models.ManyToManyField(related_name='elements', to='pokemon_entities.PokemonElementType', verbose_name='типы стихий'),
        ),
    ]
