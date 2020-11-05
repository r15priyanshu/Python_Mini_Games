#rock , paper , scissors GAME
#---------------------------------
from random import randint
print("WELCOME TO ROCK,PAPER AND SCISSORS GAME!!")
print("-------------------------------------------\n\n")

choice ="y"
while choice=="y":
    #player move
    player = input("Player , make your move: ").lower()

    rand_num = randint(0,2)
    if rand_num == 0:
            computer = "rock"
    elif rand_num == 1:
            computer = "paper"
    else:
            computer = "scissors"

    print(f"Computer plays : {computer}" )

    if player == computer:
            print("It's a tie!")
    elif player == "rock":
            if computer == "scissors":
                    print("player wins!")
            else:
                    print("computer wins!")
    elif player == "paper":
            if computer == "rock":
                    print("player wins!")
            else:
                    print("computer wins!")
    elif player == "scissors":
            if computer == "paper":
                    print("player wins!")
            else:
                    print("computer wins!")	
    else:
            print("Please enter a valid move!")

    print("----------------------")
    print("\nDO YOU WANT TO PLAY MORE (Y/N)?")
    choice=input().lower()
