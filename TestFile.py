import random

guesscount = 0
guesslimit = 5

randomnumber = random.randint(0, 10)


while guesscount < guesslimit:
    user_input = int(input("Guess a number: "))
    guesscount += 1
    if user_input == randomnumber:
        print("You guessed the correct number!")
        break
    else:
        print("Sorry, Try Again!")
