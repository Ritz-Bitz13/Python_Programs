#Martin Barber - 100368442
#Nov 3rd, 2021
#ICE 9 - Tuples & Lists
#

#input from system to use system  codes
from os import system
from colorama import Fore

#set console title
system("title Ice 9: Example 1 - Martin Barber")

#Tuple of strings
#            0      1        2        3       4
animals = ("Dog", "Cat", "Chicken", "Pig", "T-Rex", "Fox") #Error

######## Forward order
for index in range (len(animals)):

    print(f"Index {index} you have: {animals[index]}")

print("====================================")

######## Reverse order
for index2 in range (len(animals)-1,-1,-1):

    print(f"Index {index2} you have: {animals[index2]}")


#Exit Prompt
input("Press [enter] to exit: ")