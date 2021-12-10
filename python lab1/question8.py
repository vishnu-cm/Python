#Generate a random number between 1 and 9 (including 1 and 9). 
# Ask the user to guess the number, then tell them whether they guessed too low, too high, or exactly right

import random


minimum = 1
maximum = 9
number = random.randint(minimum, maximum)
guess = None
another = None
TRY = 0
running = True


while running:
    guess = input("What is your lucky number? ")

    if int(guess) < number:
        print ("Wrong, too low.")

    elif int(guess) > number:
        print ("Wrong, too high.")
    
    elif int(guess) == number:
        print ("Yes exactly the one, %s." % str(number))

    x = input ("Do you want to continue? (Y/N):  ").upper()
    if x == 'N':
            break  
        