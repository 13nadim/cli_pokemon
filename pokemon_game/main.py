# pokemon_game/main.py
# Person C: runs the game (user input + calling API + calling battle)

from api2 import get_pokemon, get_random_pokemon
from battle import battle


def print_pokemon(pokemon: dict, label: str) -> None:
    """Print a simple summary of a Pokémon."""
    print(f"\n--- {label} ---")
    print(f"Name: {pokemon['name'].title()}")
    print(f"Ability: {pokemon['ability']}")
    print(f"Height: {pokemon['height_m']} m")
    print(f"Weight: {pokemon['weight_kg']} kg")
    print(f"Stats: {pokemon['stats']}")


def get_player_pokemon() -> dict:
    """
    Ask the player if they want to choose a Pokémon by name.
    If not, give them a random Pokémon.
    """
    choice = input("Do you want to choose your Pokémon? (y/n): ").strip().lower()

    if choice == "y":
        while True:
            name = input("Enter Pokémon name (e.g. pikachu): ").strip().lower()
            player = get_pokemon(name)

            if player is not None:
                return player

            print("Pokémon not found. Please try again.")
    else:
        return get_random_pokemon()


def main():
    print("Welcome to Pokémon Battle!\n")

    # Player Pokémon
    player_pokemon = get_player_pokemon()

    # CPU Pokémon (random)
    cpu_pokemon = get_random_pokemon()

    # Show both Pokémon
    print_pokemon(player_pokemon, "Your Pokémon")
    print_pokemon(cpu_pokemon, "CPU Pokémon")

    # Run battle (Person B logic)
    print("\nStarting battle...")
    winner = battle(player_pokemon, cpu_pokemon, show_rounds=True)

    # Winner is returned as a Pokémon dictionary
    print("\n=== Final Result ===")
    print(f"Winner: {winner['name'].title()}")


if __name__ == "__main__":
    main()
