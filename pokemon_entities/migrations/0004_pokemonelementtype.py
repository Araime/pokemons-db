# Generated by Django 3.1.12 on 2021-06-15 12:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pokemon_entities', '0003_auto_20210615_1508'),
    ]

    operations = [
        migrations.CreateModel(
            name='PokemonElementType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='стихии')),
            ],
        ),
    ]
