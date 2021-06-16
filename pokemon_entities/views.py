import folium
from django.shortcuts import render
from django.http import Http404
from pokemon_entities.models import Pokemon, PokemonEntity


MOSCOW_CENTER = [55.751244, 37.618423]
DEFAULT_IMAGE_URL = (
    'https://vignette.wikia.nocookie.net/pokemon/images/6/6e/%21.png/revision'
    '/latest/fixed-aspect-ratio-down/width/240/height/240?cb=20130525215832'
    '&fill=transparent'
)


def add_pokemon(folium_map, lat, lon, image_url=DEFAULT_IMAGE_URL, pokemon_info_on_map=''):
    icon = folium.features.CustomIcon(
        image_url,
        icon_size=(50, 50),
    )
    folium.Marker(
        [lat, lon],
        popup=pokemon_info_on_map,
        icon=icon,
    ).add_to(folium_map)


def show_all_pokemons(request):
    pokemon_entities = PokemonEntity.objects.select_related('pokemon').all()
    folium_map = folium.Map(location=MOSCOW_CENTER, zoom_start=12)
    for pokemon_entity in pokemon_entities:
        add_pokemon(
            folium_map,
            pokemon_entity.lat,
            pokemon_entity.lon,
            request.build_absolute_uri(pokemon_entity.pokemon.image.url),
            pokemon_info_on_map=get_pokemon_info(pokemon_entity)
        )

    pokemons = Pokemon.objects.all()
    pokemons_on_page = []
    for pokemon in pokemons:
        pokemons_on_page.append({
            'pokemon_id': pokemon.id,
            'img_url': pokemon.image.url,
            'title_ru': pokemon.title_ru,
        })

    return render(request, 'mainpage.html', context={
        'map': folium_map._repr_html_(),
        'pokemons': pokemons_on_page,
    })


def show_pokemon(request, pokemon_id):
    try:
        pokemon = Pokemon.objects.get(id=pokemon_id)
    except Pokemon.DoesNotExist:
        raise Http404('Увы, покемон не найден!')
    previous_evolution = pokemon.previous_evolution
    next_evolution = pokemon.evolutions.all()

    if previous_evolution:
        previous_evolution = {
            'title_ru': previous_evolution.title_ru,
            'pokemon_id': previous_evolution.id,
            'img_url': previous_evolution.image.url
        }

    if next_evolution:
        next_evolution = {
            'title_ru': next_evolution[0].title_ru,
            'pokemon_id': next_evolution[0].id,
            'img_url': next_evolution[0].image.url
        }

    elements = pokemon.element_type.all()
    pokemon_elements = []
    if elements:
        for element in elements:
            pokemon_elements.append({
                'title': element.title,
                'img': element.image.url,
                'strong_against': list(element.strong_against.all())
            })

    pokemon_info = {
        'pokemon_id': pokemon_id,
        'title_ru': pokemon.title_ru,
        'title_en': pokemon.title_en,
        'title_jp': pokemon.title_jp,
        'description': pokemon.description,
        'img_url': pokemon.image.url,
        'next_evolution': next_evolution,
        'previous_evolution': previous_evolution,
        'element_type': pokemon_elements
    }

    pokemon_entities = pokemon.pokemon_entities.all()
    folium_map = folium.Map(location=MOSCOW_CENTER, zoom_start=12)
    for pokemon_entity in pokemon_entities:
        add_pokemon(
            folium_map,
            pokemon_entity.lat,
            pokemon_entity.lon,
            request.build_absolute_uri(pokemon_entity.pokemon.image.url),
            pokemon_info_on_map=get_pokemon_info(pokemon_entity)
        )

    return render(request, 'pokemon.html', context={
        'map': folium_map._repr_html_(), 'pokemon': pokemon_info
    })


def get_pokemon_info(pokemon_entity):
    pokemon_info_on_map = f'<b>{pokemon_entity.pokemon.title_ru}</b>\n' \
                   f'Уровень-<i>{pokemon_entity.level}\n</i>' \
                   f'Здоровье-<i>{pokemon_entity.health}\n</i>' \
                   f'Сила-<i>{pokemon_entity.strength}\n</i>' \
                   f'Защита-<i>{pokemon_entity.defence}\n</i>' \
                   f'Выносливость-<i>{pokemon_entity.stamina}</i>'
    return pokemon_info_on_map
