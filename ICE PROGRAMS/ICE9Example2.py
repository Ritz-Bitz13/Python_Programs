#Martin Barber - 100368442
#Nov 3rd, 2021
#ICE 9 - Tuples & Lists
#

#input from system to use system  codes
from os import system
from colorama import Fore

#set console title
system("title Ice 9: Example 2 - Martin Barber")

#Tuple of strings
#            0      1        2        3       4       5
animals = ("Dog", "Cat", "Chicken", "Pig", "T-Rex", "Fox") #Error

#Ask for animal
lost_animal = input("Hey, what animal did you lose? ")

#Did not find animal yet
found = False

#Try to find the lost animal
for index in range(len(animals)):
    #Incase we find the lost animal
    if lost_animal == animals[index]:
        #Then we print the animal name
        print(f"Found {lost_animal} at index: {index}")
        found = True
        break #We found the animal so, Stop the loop

if not found:
    print(f"Could not find the {lost_animal}")

#Exit Prompt
input("Press [enter] to exit: ")