#Martin Barber - 100368442
#Nov 12th, 2021
#ICE 11 - Bubble Sort
#

#input from system to use system  codes
from os import system
from colorama import Fore

#CONSTANTS
LIST_LENGTH = 5

#set console title
system("title Ice 11: Bubble Sort - Martin Barber")

#Create an empty list with a capacity for 5 elements
numbers_list = [None] * LIST_LENGTH

#Input loop - Ask for 5 elements and add them to the list
index = 0 #Start at index 0
while index != LIST_LENGTH:
    #Ask for a number
    number_input = input(f"Enter a number to insert at index {index}: ")

    #Check if input is numeric
    try:
        number_input = int(number_input)
        numeric = True
    except:
        numeric = False

    #Incase input is not numeric
    if not numeric:
        print(Fore.LIGHTRED_EX + "Error - Number is not numeric" + Fore.RESET)

    #Only increases the index, if input is numeric
    #Incase number is numeric
    else:
        #Add number to the list
        numbers_list[index] = number_input
        index += 1 #Go to next index

#NOTE ONLY REACHES THIS POINT AFTER GETTING A VALID LIST

#Print the list
print("Unsorted List: ")
for number in numbers_list :
    print(number, end=" ")


#Sort the list using bubble sort
sorted = False #Keep sorting until the list is sorted
while not sorted: #Keep sorting until the list is sorted

    #Set sorted to true incase it is sorted
    sorted = True
    #Go through the list
    for index in range(0,LIST_LENGTH-1):
        if numbers_list[index] >= numbers_list[index+1]:
            #Swap TRADITIONAL
            #store = numbers_list[index]
            #numbers_list[index] = numbers_list[index+1]
            #numbers_list[index+1] = store

        #SWAP PYTHONIC WAY
        #               current                next                     next                 current

            numbers_list[index], numbers_list[index +1] = numbers_list[index+1], numbers_list[index]
            sorted = False

#Print the sorted list
print("\nSorted List: ")
for number in numbers_list :
    print(number, end=" ")

#Exit Prompt
input("\nPress [enter] to exit: ")