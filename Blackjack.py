#Let's Play Black Jack

Cards = ['2 of Spades', '3 of Spades', '4 of Spades', '5 of Spades', '6 of Spades', '7 of Spades', '8 of Spades', '9 of Spades' , '10 of Spades', 'Jack of Spades', 'Queen of Spades', 'King of Spades', 'Ace of Spades', '2 of Hearts', '3 of Hearts', '4 of Hearts', '5 of Hearts', '6 of Hearts', '7 of Hearts', '8 of Hearts', '9 of Hearts' , '10 of Hearts', 'Jack of Hearts', 'Queen of Hearts', 'King of Hearts', 'Ace of Hearts', '2 of Clubs', '3 of Clubs', '4 of Clubs', '5 of Clubs', '6 of Clubs', '7 of Clubs', '8 of Clubs', '9 of Clubs' , '10 of Clubs', 'Jack of Clubs', 'Queen of Clubs', 'King of Clubs', 'Ace of Clubs', '2 of Diamonds', '3 of Diamonds', '4 of Diamonds', '5 of Diamonds', '6 of Diamonds', '7 of Diamonds', '8 of Diamonds', '9 of Diamonds' , '10 of Diamonds', 'Jack of Diamonds', 'Queen of Diamonds', 'King of Diamonds', 'Ace of Diamonds']
Card_Value = [2, 3, 4 , 5, 6, 7, 8, 9, 10, 10, 10, 11, 2, 3, 4 , 5, 6, 7, 8, 9, 10, 10, 10, 11, 2, 3, 4 , 5, 6, 7, 8, 9, 10, 10, 10, 11, 2, 3, 4 , 5, 6, 7, 8, 9, 10, 10, 10, 11,]
Actions1 = ['Hit', 'Split', 'Double Down', 'Insurance', 'Surrender']
Actions2 = ['Hit', 'Stand', 'Double Down']

Player_Hand1 = []
Player_Hand1_Value = 0
Player_Hand2 = []
Player_Hand2_Value = 0
Dealer_Hand = []
Dealer_Hand_Value = 0
Player_Chips = 200
Bet = 0
Insurance_Bet = 0
Player = 'Player'
Match = "Unknown"
Action = "Play"
Split = False

import random

def Deal():
    L = 0
    while L != 4:
        X = random.choice(Cards)
        if L == 0 or L == 2:
            Player_Hand1.append(X)
            Cards.remove(X)
            Y = Cards.index(X)
            Z = Card_Value[Y]
            Player_Hand1_Value = Player_Hand1_Value + Z
            L = L + 1
        else:
            Dealer_Hand.append(X)
            Cards.remove(X)
            Y = Cards.index(X)
            Z = Card_Value[Y]
            Dealer_Hand_Value = Dealer_Hand_Value + Z
            L = L + 1

    global Player
    while Player != 'Ready':
        if Player == 'Player':
            Evaluate()
            Player = 'Dealer'
        else:
            Evaluate()
            Player = 'Ready'
    pass

def Hit():
    X = random.choice(Cards)
    Player_Hand1.append(X)
    Cards.remove(X)
    Evaluate()
    pass

def Split():
    X = random.choice(Player_Hand1)
    Player_Hand2.append(X)
    Player_Hand1.remove(X)
    X = random.choice(Cards)
    Player_Hand1.append(X)
    Cards.remove(X)
    X = random.choice(Cards)
    Player_Hand2.append(X)
    Cards.remove(X)
    Split = True
    Evaluate()
    pass

def Double_Down():
    Player_Chips = Player_Chips - Bet
    Bet = Bet * 2
    X = random.choice(Cards)
    Player_Hand1.append(X)
    Cards.remove(X)
    Evaluate()
    Action = "Stand"
    pass

def Insurance():
    Insurance_Bet = Bet / 2
    Insurance_Bet = round(Insurance_Bet)
    pass

def Surrender():
    Player_Chips = Player_Chips + (Bet / 2)
    Match = "Loss"
    pass


while Match != "End":
    Y = Cards.index('King of Spades')
    print(Y)
    break
    Deal()
    print(Player_Hand1)
    print(Player_Hand1_Value)
    print(Actions1)
    Action = input('What is your next move? ')
    Player = 'Player'
    while Action != "Stand":
        if Action == "Hit":
            Hit()
        elif Action == "Split":
            Split()
        elif Action == "Double Down":
            Double_Down()
        elif Action == "Insurance":
            Insurance()
        else:
            Surrender()
        print(Player_Hand1)
        print()
        print(Actions2)
        Action = input('What is your next move? ')
    Player = 'Dealer'

