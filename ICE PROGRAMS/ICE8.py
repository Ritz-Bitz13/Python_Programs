#Martin Barber - 100368442
#Oct 20th, 2021
#ICE 8 - Pyramid Generator
# The user will enter a number and the program will make an Asterisk Pyramid

#input from system to use system  codes
from os import system
from colorama import Fore, Style #pip install colorama

#CONSTANTS
MIN, MAX = 5, 50
PYRAMID_START = 1
valid = False
INTRO = """
=======================
=====  Pyramid  =======
=======================

Hey! Do you want to draw and amazing Pyramid? 
Tell me the height and I will draw it for you!
"""


#set console title
system("title Ice8: Pyramid Generator  - Martin Barber")

print(INTRO)

while valid == False:
    height = input(f"Enter Height [Min: {MIN}  Max: {MAX}]: ")

    try:
        #Try to convert height
        height = int(height)
        numeric = True

    except:
        numeric = False

    if not numeric:
        print(Fore.LIGHTRED_EX +"Error - Height must be numeric!"+ Style.RESET_ALL)
    elif height < MIN or height > MAX:
        print(Fore.LIGHTRED_EX + f"Error - Please enter a number between {MIN} and {MAX}" + Style.RESET_ALL)
    else:
        valid = True

for count_lines in range (PYRAMID_START, height+1,1):
    # '':2'' means use 2 spaces
    print(f"{count_lines:2}", end="") #***end=""*** means keep printing in the same line
    # CAlculate how many spaces
    spaces = height - count_lines
    #Draw Spaces
    for count in range(0, spaces):
        print (" ", end="") #
    #Draw the Asterisks
    for astrisk in range (0,count_lines):
        print(" *", end="")
    # Finish Line
    print("")


#Exit Prompt
input("Press [enter] to exit: ")