''''''
# 3. Create a basic rock paper scissors game.
# Take 2 user inputs from 2 players. You can use R, P and S are possible user inputs. Play the game
# for 10 rounds and declare the winner.
# Rules of the game
# Rock vs Scissors - Rock wins
# Rock vs Paper - Paper wins
# Paper vs Scissors - Scissor wins
# Eg: Game 1: Player1 = R, Player2 = S, Output: Player1 wins
# Player1 = P, Player2 = P, Output: Draw
# Final Winner: Player with maximum wins
# # ''''''

from random import randint
# moves for the players
Moves =["rock","paper","scissors"]

while True:
    Computer = Moves[randint(0,2)]
    Player = input("rock ,paper or scissors (or End of the game):").lower()

    if Player == "End the game":
        print("The gane has ended")
        break
    elif Player == Computer:
        print ("Draw !!")
    elif Player =="rock":
        if Computer == "paper":
            print("Papar lose! ", Computer)
        else :
            print("Papar win!", Player)
    elif Player == "paper":
        if Computer == "scissors":
            print("scissors lose! ", Computer)
        else:
            print("scissors win!", Player, "beats", Computer)

    elif Player == "scissors":
        if Computer == "rock":
            print("Rock lose! ", Computer)
        else:
            print("Rock win!", Player )
    else:
        print("Check your spelling")




