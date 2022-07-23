#Martin Barber - 100368442
#Oct  6th, 2021
#ICE 6 - Guess the number
#Game that the player has to guess a secret random number

#input from system to use system codes
from os import system

import random #Allows us to generate random numbers

MIN_NUMBER, MAX_NUMBER = 1, 100

#set console title
system("title Ice6: Guess the Number - Martin Barber")

#We want to play at least once! So we need to set the value for restart
restart = "r"


#Restart the game if the player hits R:
while restart.lower() == "r":

    #clear screen for a new game
    system("cls")
    #Generate a random number to play
    magic_number = random.randint(MIN_NUMBER, MAX_NUMBER)

    counter = 1
    #Start with a guess that is not valiud, so we can play!
    guess_number = 0

    #Keep playing until the player guesses the secret number
    while guess_number != magic_number:
        

        
        #Have the player guess a number
        guess_number = input(f"Pick a number between {MIN_NUMBER} and {MAX_NUMBER}: ")

        #Try to convert it to an integer
        try:
            guess_number = int(guess_number)
            numeric = True #Able to convert

        #If you cant convert, it fails
        except:
            numeric = False #unable to convert

        #Not numeric must print an error message.
        if not numeric:
            print("Error - Invalid input!")

        #Print an error is the guess is not in the valid range
        elif guess_number < MIN_NUMBER or guess_number > MAX_NUMBER:
            print(f"Error - You must select a number between {MIN_NUMBER} and {MAX_NUMBER}")

        #Valid Guess, Give a hint
        else:
            #Guess is too low
            if guess_number > magic_number:
                print(f"{guess_number} is too high")
                counter += 1
        
            #Guess is too high
            elif guess_number < magic_number:
                print(f"{guess_number} is too low")
                counter += 1

    print(f"Hurray! Yes, the number was {magic_number}!")
    print(f"You guessed the right number in {counter} attempts.")

    

    #Ask player if they want to restart
    restart = input("Press [r] to restart: ")