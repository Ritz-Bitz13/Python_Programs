#Martin Barber - 100368442
#Nov 10th, 2021
#ICE 10 - Left Circular Shift
#Shift a list to the left by a given amount of times

#input from system to use system  codes
from os import system
from colorama import Fore


INTRO = """=========================
== Left Circular Shift ==
=========================
"""

restart = "r"

#set console title
system("title Ice 10 Left Circular Shift - Martin Barber")


while restart == "r":
    accept = False
    #clear the console
    system("cls")
    #Draw a banner everytime the app restarts
    elements = input(INTRO + "Enter elements separated by spaces: ").split()

    #Validation loop
    while not accept:
        
        shifts = input("\nHow many times will you like to shift: ")
        try:
            shifts = int(shifts)
            numeric = True
        except:
            numeric = False
    
        #Accept input when shifts is a positive, whole number
        accept = numeric and shifts > 0
        #Error message
        if not accept:
            print(Fore.LIGHTRED_EX + "Error - Shifts must be a positive, whole number!" + Fore.RESET)


    #Loop as many times as given to shift
    for count_shifts in range(0, shifts):
        #We need to copy the original element
        original_first = elements[0]

        #Shift the element of the list to the left
        #go through all indexes of the list except the last one
        for index in range(len(elements)-1):
            #copy the next element into the current index
            elements[index] = elements[index+1]

        #copy original first element and input it to the last slot of the list
        elements[len(elements)-1] = original_first


    #Print the list called elements
    for element in elements:
        print(element, end= " ")


    #Exit Prompt    
    restart = input("\nPress [r] to restart: ").lower()