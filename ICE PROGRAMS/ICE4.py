#Martin Barber - 100368442
#Sept 29th, 2021
#ICE 4 Dice Bet - Random Numbers
#Try to predict the 2 dice added together

#input from system to use system  codes
from os import system

import random #Allows us to generate random numbers


#set console title
system("title Ice4: Dice Bet - Martin Barber")

#Constants
MIN_BET, MAX_BET = 2,12
MIN_DICE, MAX_DICE = 1, 6

#Ask the user to place a bet
bet_number = input(f"Place a bet between {MIN_BET} and {MAX_BET}: ")

try:
    bet_number = int(bet_number)
    numeric = True #Able to convert


except:
    numeric = False #Not able to convert


#If the bet is not numeric, then print an error
if not numeric:
    print("Bet is not Numeric!")

#If the bet is not in the valid range, then print an error
elif bet_number < MIN_BET or bet_number > MAX_BET:
    print(f"Your bet must be between {MIN_BET} and {MAX_BET}")

#Valid Bet, We can play 
else:
    #Roll the two dice
    dice_one = random.randint(MIN_DICE,MAX_DICE)
    dice_two = random.randint(MIN_DICE, MAX_DICE)

    #Add the 2 dice together
    dice_total = dice_one + dice_two

    #Print guess and dice result
    print(f"Your bet: {bet_number}")
    print(f"Dice Result: {dice_one} + {dice_two} = {dice_total}")

    #If the dice total = your guess you are right
    if dice_total == bet_number:
        print("You are correct! Congratulations!")

    #  If your guess is different from the dice total, you are wrong
    else:
        print("Sorry you were incorrect.")


#Exit Prompt
input("Press ENTER to exit: ")