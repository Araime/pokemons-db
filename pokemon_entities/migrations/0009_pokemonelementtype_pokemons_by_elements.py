# Generated by Django 3.1.12 on 2021-06-15 21:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pokemon_entities', '0008_auto_20210615_2152'),
    ]

    operations = [
        migrations.AddField(
            model_name='pokemonelementtype',
            name='pokemons_by_elements',
            field=models.ManyToManyField(related_name='pokemons_by_type', to='pokemon_entities.Pokemon', verbose_name='покемоны'),
        ),
    ]
