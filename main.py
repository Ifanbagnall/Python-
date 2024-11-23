import random

class Pokemon:
    def __init__(self, name, health, moves):
        self.name = name
        self.health = health
        self.moves = moves  # A dictionary with move name as key and damage as value

    def attack(self, move_name, opponent):
        if move_name in self.moves:
            damage = self.moves[move_name]
            opponent.health -= damage
            print(f"{self.name} used {move_name}!")
            print(f"It dealt {damage} damage to {opponent.name}!")
        else:
            print(f"{self.name} doesn't know {move_name}!")

    def is_fainted(self):
        return self.health <= 0

    def __str__(self):
        return f"{self.name}: {self.health} HP"

# Define Pokémon
pikachu = Pokemon("Pikachu", 100, {"Thunder Shock": 20, "Quick Attack": 15})
charmander = Pokemon("Charmander", 100, {"Ember": 20, "Scratch": 10})

# Game loop
def battle(pokemon1, pokemon2):
    print("A wild battle begins!")
    print(f"{pokemon1} vs {pokemon2}\n")

    while True:
        # Player 1's turn
        print(f"\n{pokemon1.name}'s turn!")
        print("Available moves:", ", ".join(pokemon1.moves.keys()))
        move = input("Choose a move: ").strip()
        pokemon1.attack(move, pokemon2)

        if pokemon2.is_fainted():
            print(f"{pokemon2.name} fainted! {pokemon1.name} wins!")
            break

        # Player 2's turn
        print(f"\n{pokemon2.name}'s turn!")
        move = random.choice(list(pokemon2.moves.keys()))  # AI chooses a random move
        pokemon2.attack(move, pokemon1)

        if pokemon1.is_fainted():
            print(f"{pokemon1.name} fainted! {pokemon2.name} wins!")
            break

        # Show status
        print(f"\n{pokemon1}")
        print(f"{pokemon2}")

# Start the battle
battle(pikachu, charmander)
