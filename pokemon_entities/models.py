from django.db import models


class PokemonElementType(models.Model):
    title = models.CharField('стихии', max_length=200)
    image = models.ImageField('изображение', upload_to='elements', null=True, blank=True)
    strong_against = models.ManyToManyField('self', symmetrical=False, null=True, blank=True,
                                            verbose_name='силен против')

    def __str__(self):
        return self.title


class Pokemon(models.Model):
    title_ru = models.CharField('название на русском', max_length=200)
    title_en = models.CharField('название на английском', max_length=200, blank=True)
    title_jp = models.CharField('название на японском', max_length=200, blank=True)
    image = models.ImageField('изображение', upload_to='pokemons', null=True, blank=True)
    description = models.TextField('описание', blank=True)
    element_type = models.ManyToManyField(PokemonElementType, blank=True, verbose_name='типы стихий',
                                          related_name='elements')
    previous_evolution = models.ForeignKey('Pokemon', on_delete=models.SET_NULL, null=True, blank=True,
                                           verbose_name='эволюционировал из', related_name='evolutions')

    def __str__(self):
        return self.title_ru


class PokemonEntity(models.Model):
    pokemon = models.ForeignKey(Pokemon, on_delete=models.CASCADE, verbose_name='покемон',
                                related_name='pokemon_entities')
    lat = models.FloatField('широта')
    lon = models.FloatField('долгота')
    appeared_at = models.DateTimeField('появится', null=True, blank=True)
    disappeared_at = models.DateTimeField('исчезнет', null=True, blank=True)
    level = models.IntegerField('уровень', null=True, blank=True)
    health = models.IntegerField('здоровье', null=True, blank=True)
    strength = models.IntegerField('сила', null=True, blank=True)
    defence = models.IntegerField('защита', null=True, blank=True)
    stamina = models.IntegerField('выносливость', null=True, blank=True)

    def __str__(self):
        return f'Покемон {self.pokemon}, уровень {self.level}'
