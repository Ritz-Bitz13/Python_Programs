#Martin Barber - 100368442
#Nov 3rd, 2021
#ICE 9 - Tuples & Lists
#

#input from system to use system  codes
from os import system
from colorama import Fore

#set console title
system("title Ice 9: Example 4 - Martin Barber")

animals = ["Dog", "Cat", "Chicken", "Pig", "T-Rex", "Fox"]

found = False
#Ask for a letter
start_char = input("You want all animals starting with the letter: ")

#search all animals that start with the letter
for animal in animals:
#Go through all the animals
    if start_char.upper() == animal[0]:
        found = True
    #Compare the start_char and the 1st letter of each animal

        #If the letters are the same

        #Then Print the animal
        print(animal)

if not found:
    print(f"Sorry, we didnt have any animal that begins with {start_char}")



#Exit Prompt
input("Press [enter] to exit: ")