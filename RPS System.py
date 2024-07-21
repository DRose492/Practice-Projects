# This code is meant to simulate a match of Rock, Paper, Scissors against an computer opponent
Match = input("Would you like to play a match of Rock, Paper, Scissors? Y or N? ")
Draw = 0
Wins = 0
Losses = 0
while Match.upper() == "Y":
    Player_Choice = input("What do you choose? Rock, Paper, or Scissors? ")
    Choices = ["ROCK", "PAPER", "SCISSORS"]
    import random
    Computer_Choice = random.choice(Choices)
# These statement determine what case scenario is to be used
    if Player_Choice.upper() == "ROCK":
            N = 1
    elif Player_Choice.upper() == "PAPER":
            N = 2
    else:
            N = 3
# These clusters are each scenario playing out
    if N == 1:
        if Computer_Choice == "ROCK":
            Draw += 1
            print("The computer also chose that. It's a draw.")
        elif Computer_Choice == "PAPER":
            Losses += 1
            print("The computer chose paper. Looks like you lost this round.")
        else:
            Wins += 1
            print("The computer chose scissors. You won this round!")
    elif N == 2:
        if Computer_Choice == "ROCK":
            Wins += 1
            print("The computer chose rock. You won this round!")
        elif Computer_Choice == "PAPER":
            Draw += 1
            print("The computer also chose that. It's a draw.")
        else:
            Losses += 1
            print("The computer chose scissors. Looks like you lost this round.")
    else:
        if Computer_Choice == "ROCK":
            Losses += 1
            print("The computer chose rock. Looks like you lost this round.")
        elif Computer_Choice == "PAPER":
            Wins += 1
            print("The computer chose paper. You won this round!")
        else:
            Draw += 1
            print("The computer also chose that. It's a draw.")
    Stats = input("Would you like to see how you've done? Y or N ")
# This allows the system to keep track of wins, losses, and draws while playing
    while Stats.upper() == "Y":
        if Wins > 1:
            print("You have won " + str(Wins) + " games.")
        else:
            print("You have won " + str(Wins) + " game.")
        if Losses > 1:
            print("You have lost " + str(Losses) + " games.")
        else:
            print("You have lost " + str(Losses) + " game.")
        if Draw > 1:
            print("And you have tied " + str(Draw) + " games.")
        else:
            print("And you have tied " + str(Draw) + " game.")
        break
    Match = input("Would you like to play another round? Y or N ")
