import random

EnemyMoveList = ["LightAtk", "Dodge", "HeavyAtk", "Ultimate"]
PlayerMoveList = ["LightAtk", "HeavyAtk", "Dodge", "Block", "Parry", "Ultimate"]
Class = ""
Level = ""
Weapon = ""

class Player:
    def __init__(self, H, A, D):
        self.Health = H
        self.Attack = A
        self.Defense = D
        self.Class = None
        self.Weapon = None
        self.Armor = None
        self.Level = 1
        self.LightAtk = WeaponPower() + self.Attack
        self.HeavyAtk = (WeaponPower() + self.Attack) * 2
        self.Dodge = 90
        self.Block = self.Defense * 2

def WeaponPower():
    if Weapon == None:
        if Class == "Monk":
            return 1 + Level
        else:
            return 1
    elif Weapon == "Dagger":
        if Class == "Rogue":
            return 5 + Level
        else:
            return 5
    elif Weapon == "Sword":
        return 10
    elif Weapon == "Staff":
        return 3

Guy = Player(50, 12, 1)

print(Guy.Health + " Health")
print(Guy.Attack + " Attack Power")
print(Guy.Defense + " Defense")