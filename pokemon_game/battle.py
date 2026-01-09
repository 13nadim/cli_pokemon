# alex

import random

# 1) STAT HELPERS

def get_stat(pokemon: dict, stat_name: str) -> int:
    return int(pokemon["stats"][stat_name])


def apply_ability_bonus(pokemon: dict) -> dict:

    ability = pokemon["ability"].lower()
    boosted = pokemon.copy()
    boosted["stats"] = pokemon["stats"].copy()

    # Simple keyword-based bonuses
    if "speed" in ability:
        boosted["stats"]["speed"] += 10
    elif "power" in ability or "strong" in ability:
        boosted["stats"]["attack"] += 10
    elif "shield" in ability or "armor" in ability:
        boosted["stats"]["defense"] += 10
    elif "heal" in ability or "regen" in ability:
        boosted["stats"]["hp"] += 10

    return boosted


# 2) DAMAGE CALCULATION

def calculate_damage(attacker: dict, defender: dict) -> int:

    attack = get_stat(attacker, "attack")
    defense = get_stat(defender, "defense")

    # Base formula (always at least 1)
    base_damage = max(1, attack - (defense // 2))

    # Add small randomness
    variance = random.randint(-2, 2)
    damage = max(1, base_damage + variance)

    # Critical hit chance
    if random.random() < 0.10:
        damage *= 2
        print("  Critical hit!")

    return damage


# 3) TURN ORDER

def choose_turn_order(player1: dict, player2: dict) -> tuple:

    speed1 = get_stat(player1, "speed")
    speed2 = get_stat(player2, "speed")

    if speed1 > speed2:
        return player1, player2
    if speed2 > speed1:
        return player2, player1

    # Speed tie
    return random.choice([(player1, player2), (player2, player1)])


# 4) ONE BATTLE

def battle(player1: dict, player2: dict, show_rounds: bool = True) -> dict:

    p1 = apply_ability_bonus(player1)
    p2 = apply_ability_bonus(player2)

    # Starting HP
    p1_hp = get_stat(p1, "hp")
    p2_hp = get_stat(p2, "hp")

    # Choose who goes first
    first, second = choose_turn_order(p1, p2)

    # Make sure HP variables match who is first/second
    if first == p1:
        first_hp, second_hp = p1_hp, p2_hp
    else:
        first_hp, second_hp = p2_hp, p1_hp

    round_num = 1

    while first_hp > 0 and second_hp > 0:
        if show_rounds:
            print(f"\nRound {round_num}")

        # First attacks second
        damage = calculate_damage(first, second)
        second_hp = max(0, second_hp - damage)

        if show_rounds:
            print(f"{first['name'].title()} hits {second['name'].title()} for {damage} damage!")
            print(f"{second['name'].title()} HP: {second_hp}")

        if second_hp == 0:
            if show_rounds:
                print(f"\nWinner: {first['name'].title()}")
            return first

        # Second attacks first
        damage = calculate_damage(second, first)
        first_hp = max(0, first_hp - damage)

        if show_rounds:
            print(f"{second['name'].title()} hits {first['name'].title()} for {damage} damage!")
            print(f"{first['name'].title()} HP: {first_hp}")

        if first_hp == 0:
            if show_rounds:
                print(f"\nWinner: {second['name'].title()}")
            return second

        round_num += 1

    # Fallback (should not reach)
    return first if first_hp > 0 else second


# 5) BEST OF 3 MODE (OPTIONAL)

def best_of_three(player1: dict, player2: dict) -> dict:

    wins_1 = 0
    wins_2 = 0
    match_num = 1

    while wins_1 < 2 and wins_2 < 2:
        print(f"\n=== Match {match_num} ===")

        winner = battle(player1, player2, show_rounds=False)

        if winner["name"] == player1["name"]:
            wins_1 += 1
            print(f"{player1['name'].title()} wins this match! ({wins_1} - {wins_2})")
        else:
            wins_2 += 1
            print(f"{player2['name'].title()} wins this match! ({wins_1} - {wins_2})")

        match_num += 1

    overall_winner = player1 if wins_1 == 2 else player2
    print(f"\n=== Overall Winner: {overall_winner['name'].title()} ===")
    return overall_winner



