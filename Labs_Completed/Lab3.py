#Martin Barber - 100368442
#Oct 20th, 2021
#Lab 3 - Prime Number 
#Enter a number between 2 and 100 and it will find how many prime numbers there are between them.

#input from system to use system  codes
from os import system
from colorama import Fore
import math

MIN, MAX = 2, 100
INTRO = """=======================
===  Prime Numbers  ===
=======================
"""
#Set variables to start the program, if they're not defined then program will not start
valid = False
restart = "r"
#set console title
system("title Lab 3: Prime Numbers - Martin Barber")

#Print the intro of the big prime numbers start
print(INTRO)


while restart.lower() == "r":
    #Set this counter to 0 incase you restart the app at the end, so it does not add the previous prime numbers found
    counter_primes = 0

    #Set valid to False so the loop will continue to ask the question
    
    while valid == False:
        #Ask the question for the user to input a number between 2 and 100.
        input_number = input(f"\nEnter a number between {MIN} and {MAX}: ")

        #Check to see if it is numeric
        try:
            input_number = int(input_number)
            numeric = True
        
        except:
            numeric = False
        
        #If the number is not a whole number print an error
        if not numeric:
            print(Fore.LIGHTRED_EX + "Error - Input must be a whole number." + Fore.RESET)

        #If number is outside min and Max numbers print an error
        elif input_number < MIN or input_number > MAX:
            print(Fore.LIGHTRED_EX + f"Error - Number should be between {MIN} and {MAX}." + Fore.RESET)

        else:
            valid = True

    #Clears the screen
    system("cls")

    #Displays the new screen about checking all prime numbers up to the given number
    print("============================")
    print(f"== Prime Numbers up to {input_number:2} ==")
    print("============================")

    #Get the square root of the input number and turn it to int
    square_root = math.sqrt(input_number)

    #Start the loops, first get a variable to count from 2 to the number given
    for prime_count in range(MIN, input_number+1, 1):
        #Reset prime to true or else once it turns false it will never go true again
        prime = True
        #Start a loop to check that number if it is a prime or not
        for change in range(MIN, prime_count):
            result = prime_count % change
            #Once the counter gets higher than the square root, it stops the loop because there is no way it can be a prime.
            if change > square_root:
                break
            #If result has a 0 remander, it is not prime.
            if result == 0:
                prime = False
            

        # if the number is prime, then 
        if prime == True:
            #Add 1 to counter for every prime number it finds is True
            counter_primes = counter_primes + 1
            # Display the Hashtags and Number at the end
            for change in range (0, prime_count):
                print(Fore.LIGHTCYAN_EX + "#", end="" + Fore.RESET)
            print(f"{Fore.LIGHTRED_EX}{prime_count}{Fore.RESET}")

    #tell the user how many prime numbers were found between the minimum number and the number given by the user
    print(f"\nThere are {Fore.LIGHTRED_EX}{counter_primes}{Fore.RESET} prime numbers between {MIN} and {input_number}")
    
    #Exit Prompt
    restart = input("\nPress [r] to restart: ")
    #Reset valid to false to jump back to loop
    if restart == "r":
        system("cls")
        #Because we are restarting the program, resetting the Valid as False and reprints the INTRO.
        valid = False
        print(INTRO)
    #End the if statement and close program if anything but r is typed
    else:
        break