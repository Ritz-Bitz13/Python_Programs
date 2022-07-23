#Martin Barber - 100368442
#Nov 3rd, 2021
#ICE 9 - Tuples & Lists
#

#input from system to use system  codes
from os import system
from colorama import Fore

#set console title
system("title Ice 9: Example 3 - Martin Barber")

#List of strings
#            0      1        2        3       4       5
animals = ["Dog", "Cat", "Chicken", "Pig", "T-Rex", "Fox"] #Error
temp_list = []  #Empty List, 0 Elements

#Print before reversing
for animal in animals:
    print(animal)
    temp_list.insert(0, animal) #append (end of list)...... Insert (beginning of the list)

animals = temp_list
#Get rid of temp_list (assigning it to nothing)
temp_list = None


print("===============================")
#Reversing
################ EASY WAY #####################
animals.reverse()
################ HARD WAY #####################

#Print after reversing
for animal in animals:
    print(animal)


#Exit Prompt
input("Press [enter] to exit: ")