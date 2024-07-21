#Pokemon Battling

Pokemons = ['Blastois', 'Venusaur', 'Charizard', 'Butterfree', 'Beedrill', 'Pidgeot', 'Raticate', 'Arbok', 'Fearow', 'Raichu', 'Sandslash', 'Nidoqueen', 'Nidoking', 'Clefable', 'Ninetales', 'Wigglytuff', 'Golbat', 'Vileplume', 'Parasect', 'Venomoth', 'Dugtrio']

class Pokemon:
    def __init__(self, Level, Type1, Type2, HP, Attack, Defense, Special_Attack, Special_Defense, Speed):
        self.Level = Level
        self.Type1 = Type1
        self.Type2 = Type2
        self.HP = HP
        self.Attack = Attack
        self.Defense = Defense
        self.Special_Attack = Special_Attack
        self.Special_Defense = Special_Defense
        self.Speed = Speed
    def __str__(self) -> str:
        pass

Blastois = Pokemon(50, 'Water', 'Null', 154, 103, 120, 105, 125, 98)
Venusaur = Pokemon(50, 'Grass', 'Poison', 155, 102, 103, 120, 120, 100)
Charizard = Pokemon(50, 'Fire', 'Flying', 153, 104, 98, 129, 105, 120)
Butterfree = Pokemon(50, 'Bug', 'Flying', 135, 65, 70, 110, 100, 90)
Beedrill = Pokemon(50, 'Bug', 'Poison', 140, 110, 60, 65, 100, 95)
Pidgeot = Pokemon(50, 'Normal', 'Flying', 158, 100, 95, 90, 90, 121)
Raticate = Pokemon(50, 'Normal', 'Null', 130, 101, 80, 70, 90, 117)
Fearow = Pokemon(50, 'Normal', 'Flying', 140, 110, 85, 81, 81, 120)
Arbok = Pokemon(50, 'Poison', 'Null', 135, 115, 89, 85, 99, 100)
Raichu = Pokemon(50, 'Electric', 'Null', 135, 110, 75, 110, 100, 135)
Sandslash = Pokemon(50, 'Ground', 'Null', 150, 120, 130, 65, 75, 85)
Nidoqueen = Pokemon(50, 'Poison', 'Ground', 165, 112, 107, 95, 105, 96)
Nidoking = Pokemon(50, 'Poison', 'Ground', 156, 122, 97, 105, 95, 105)
Clefable = Pokemon(50, 'Fairy', 'Null', 170, 90, 93, 115, 110, 80)
Ninetales = Pokemon(50, 'Fire', 'Null', 148, 96, 95, 101, 120, 120)
Wigglytuff = Pokemon(50, 'Normal', 'Fairy', 215, 90, 65, 105, 70, 65)
Golbat = Pokemon(50, 'Poison', 'Flying', 150, 100, 90, 85, 95, 110)
Vileplume = Pokemon(50, 'Grass', 'Poison', 150, 100, 105, 130, 110, 70)
Parasect = Pokemon(50, 'Bug', 'Grass', 135, 115, 100, 80, 100, 50)
Venomoth = Pokemon(50, 'Bug', 'Poison', 145, 85, 80, 110, 95, 110)
Dugtrio = Pokemon(50, 'Ground', 'Null', 110, 120, 70, 70, 90, 140)

import random
Done = False

while Done is not True:
    X = random.choice(Pokemons)
    print(str(X.Level))
    print(X.Type1)
    print(X.Type2)
    print(str(X.HP))
    print(X.Attack)
    print(X.Defense)
    print(X.Special_Attack)
    print(X.Special_Defense)
    print(X.Speed)
    print()
    Done = input("Done? True or False")
    if Done == 'True':
        Done = True
    else:
        Done = False