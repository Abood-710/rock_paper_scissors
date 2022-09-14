import random

while True:
    choices = ["rock","paper","scissors",]


    computer = random.choice(choices)
    player = None

    while player not in choices: 
        player = input("rock, paper, or scissors?: ").lower()

    if player == computer:
        print("computer: ",computer)
        print("player: ",player)
        print("Tie!, U should play agian and win")
    elif player == "rock":
        if computer == "paper":
            print("computer: ",computer)
            print("player: ",player)
            print("You lose 🤣! Noob")
        if computer == "scissors":
            print("computer: ",computer)
            print("player: ",player)
            print("You win ! impressive😮")
    elif player == "paper":
        if computer == "scissors":
            print("computer: ",computer)
            print("player: ",player)
            print("You lose 🤣! Noob")
        if computer == "rock":
            print("computer: ",computer)
            print("player: ",player)
            print("You win ! impressive😮")
    elif player == "scissors":
        if computer == "rock":
            print("computer: ",computer)
            print("player: ",player)
            print("You lose 🤣! Noob")
        if computer == "paper":
            print("computer: ",computer)
            print("player: ",player)
            print("You win ! impressive😮")

    play_again = input("play again? (yes/No): ").lower()

    if play_again !="yes":
        break
print("adiós👋")
