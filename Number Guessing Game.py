#Number Guessing game
#----------------------------------

import random
print("WELCOME TO NUMBER GUESSING GAME")
print("---------------------------------")
random_num = random.randint(1,10) #both inclusive

choice='y'

while choice=='y' or choice=='Y':
    guess=int(input("\npick a number from ( 1-10 )  --> "))
    while True:
        if random_num==guess:
            print("YOU GUESSED IT !! :) :)")
            print("----------------------------------")
            break      
        else:
            if guess>random_num:
                print("too high !!")
                guess=int(input("guess again:"))
            else:
                print("too low !!")
                guess=int(input("guess again:"))

    
    print("Do you want to play again ? (Y,N)")
    choice=input()
    
