import requests
import random

# Base URL for all Pokémon API requests
BASE_URL = "https://pokeapi.co/api/v2/pokemon/"


def get_pokemon(name_or_id):
    """
    Fetch a Pokémon by name (e.g. "pikachu") or by ID (e.g. 25)
    from the PokéAPI.

    Returns a dictionary with basic Pokémon data:
    - name
    - height (metres)
    - weight (kilograms)
    - ability
    - battle stats (hp, attack, defense, speed)

    Returns None if the Pokémon is not found.
    """

    # Build the API URL using the name or ID
    url = BASE_URL + str(name_or_id).lower().strip()

    # Send request to the PokéAPI
    response = requests.get(url)

    # If the request failed (e.g. invalid Pokémon name)
    if response.status_code != 200:
        return None

    # Convert JSON response into a Python dictionary
    pokemon_data = response.json()

    # Get the Pokémon's first listed ability
    ability = pokemon_data["abilities"][0]["ability"]["name"]

    # Convert height and weight into readable units
    height_m = pokemon_data["height"] / 10      # decimetres → metres
    weight_kg = pokemon_data["weight"] / 10     # hectograms → kilograms

    # Extract key stats needed for battle logic
    stats = {}
    for stat in pokemon_data["stats"]:
        stat_name = stat["stat"]["name"]

        if stat_name in ["hp", "attack", "defense", "speed"]:
            stats[stat_name] = stat["base_stat"]

    # Return clean, reusable Pokémon data
    return {
        "name": pokemon_data["name"],
        "height_m": height_m,
        "weight_kg": weight_kg,
        "ability": ability,
        "stats": stats
    }


def get_random_pokemon():
    """
    Get a random Pokémon for the CPU player.
    Uses Pokémon IDs from Generation 1 (1–151).
    """

    random_id = random.randint(1, 151)
    return get_pokemon(random_id)
