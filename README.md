# Pokémon Battle Game

**A fun terminal-based Pokémon battle simulator** built in Python using real data from the **[PokéAPI](https://pokeapi.co)**.

Choose your Pokémon (or get a random one), face a CPU opponent, and battle using actual Pokémon stats!

![Pokémon Battle Banner](https://via.placeholder.com/900x300/6b7280/ffffff?text=Pokemon+Battle+Terminal+Game)

## Features

- Real Pokémon data fetched from **PokéAPI**
- Single-player mode (Player vs CPU)
- Optional two-player mode (Player vs Player)
- Choose your Pokémon or get a random one
- Turn-based battles using **HP, Attack, Defense & Speed**
- Speed determines who attacks first
- Simple but fair damage calculation

## Game Rules

| Stat | Description |
|------|-------------|
| **HP** | How much damage a Pokémon can take before fainting |
| **Attack** | Base damage output for attacks |
| **Defense** | Reduces incoming damage |
| **Speed** | Determines turn order (faster Pokémon attacks first) |

**Battle Flow:**
- Each turn, Pokémon attack each other
- Damage = `(Attacker's Attack - Defender's Defense) + random factor`
- Battle ends when one Pokémon's HP reaches 0

## Project Structure

```
cli_pokemon/
├── README.md
├── pokemon_game/
│   ├── main.py          # Main game loop and user interface
│   ├── api.py           # PokéAPI data fetching
│   ├── battle.py        # Battle logic and simulation
│   └── utils.py         # Helper functions
└── requirements.txt     # Python dependencies
```

## Tech Stack

- **Language**: Python 3.7+
- **Main library**: `requests` (for PokéAPI)
- **API**: [PokéAPI](https://pokeapi.co)

## Quick Start

### Prerequisites
- **Python 3.7+** installed on your system
- **pip** package manager

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/cli_pokemon.git
   cd cli_pokemon
   ```

2. **Install required packages**
   ```bash
   pip install requests
   ```

3. **Run the game**
   ```bash
   cd pokemon_game
   python main.py
   ```

### How to Play

1. **Choose your battle mode**
   - Single-player: Battle against CPU
   - Two-player: Battle against another player

2. **Select your Pokémon**
   - Enter a Pokémon name (e.g., "pikachu", "charizard")
   - Or type "random" for a surprise Pokémon

3. **Watch the battle unfold!**
   - Pokémon with higher speed attacks first
   - Battle continues until one Pokémon's HP reaches 0
   - Winner takes all!

## Team & Responsibilities

| Person | Role | Main Files |
|--------|------|------------|
| **Nadim** | PokéAPI data handling | `api.py` |
| **Alex** | Battle logic & simulation | `battle.py` |
| **Aamina** | Game flow, UI, documentation | `main.py`, `README.md` |

## Development Process (Agile / Scrum)

- **Project Management**: GitHub Project board
- **Workflow**: Backlog → To Do → In Progress → Review → Done
- **Version Control**: Feature branches + pull requests
- **Communication**: Team meetings

## Future Enhancements

- [ ] Pokémon type effectiveness (Fire > Grass, Water > Fire, etc.)
- [ ] Real moves and special abilities from PokéAPI
- [ ] Multiple rounds / best-of-3 battles
- [ ] Tournament mode with brackets
- [ ] Enhanced battle animations (text-based)
- [ ] Support for newer Pokémon generations (up to Gen 9)
- [ ] Save/load battle history
- [ ] Multiplayer online battles

## Contributing

1. Create your feature branch (`git checkout -b feature/amazing-feature`)
2. Commit your changes (`git commit -m 'Add amazing feature'`)
3. Push to the branch (`git push origin feature/amazing-feature`)
4. Open a Pull Request