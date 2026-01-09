import requests
import json
import random

BASE_URL = "https://pokeapi.co/api/v2/pokemon/"


def get_pokemon(name_or_id):
    """
    Fetch Pokémon data from the PokéAPI.
    Uses the same approach as taught in API lessons:
    - requests.get()
    - response.text
    - json.loads()
    """

    url = BASE_URL + str(name_or_id).lower().strip()
    response = requests.get(url)

    # Check HTTP status code (as taught)
    if response.status_code != 200:
        return None

    # Convert JSON text into Python dictionary
    pokemon_data = json.loads(response.text)

    # Extract ability
    ability = pokemon_data["abilities"][0]["ability"]["name"]

    # Convert height and weight
    height_m = pokemon_data["height"] / 10
    weight_kg = pokemon_data["weight"] / 10

    # Extract stats
    stats = {}
    for stat in pokemon_data["stats"]:
        stat_name = stat["stat"]["name"]
        if stat_name in ["hp", "attack", "defense", "speed"]:
            stats[stat_name] = stat["base_stat"]

    return {
        "name": pokemon_data["name"],
        "height_m": height_m,
        "weight_kg": weight_kg,
        "ability": ability,
        "stats": stats
    }


def get_random_pokemon():
    random_id = random.randint(1, 151)
    return get_pokemon(random_id)
