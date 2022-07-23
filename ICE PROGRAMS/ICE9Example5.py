#Martin Barber - 100368442
#Nov 4th, 2021
#ICE 9 - 
#

#input from system to use system  codes
from os import system
from colorama import Fore

#set console title
system("title Ice9: Example5 - Martin Barber")


full_name = input("What's your full name? ").split()

#Just first name
first_name = full_name[0]

#Just first name
last_name = full_name[len(full_name)-1]

print(f"My name is {last_name}, {first_name} {last_name}")


#Exit Prompt
input("Press [enter] to exit: ")