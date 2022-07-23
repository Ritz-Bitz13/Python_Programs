#Martin Barber - 100368442
#Oct 1st, 2021
#ICE 5 - Leap year calculator
#This lab will calculate the year you enter if it is a leap year

#input from system to use system  codes
from os import system

#set console title
system("title Ice5: Leap Year Calculator - Martin Barber")

#Asking what year you want to check
year_entered = input("Please enter a year: ")

try:
    #see if you can make the year entered into an Int
    year_entered = int(year_entered)
    numeric = True #If the year entered is an Int
except:
    numeric = False #year year entered isnt just numbers

#Print error incase number is not numeric
if not numeric:
    print("Error: The year must be a whole number!")

#Print an error if the year is 0
elif year_entered == 0:
    print("Error: The year can not be 0")

#Valid year, we can continue to checks
else:
    #If the year is divisable by 4 check
    if year_entered % 4 == 0:
        #only check if year is divisible by 4
        if year_entered % 100 != 0:
            print(f"{year_entered} is a leap year!")

        #if the year is divisible by 400
        elif year_entered % 400 == 0:
            print(f"{year_entered} is a leap year!")
        #If both conditions above is false then display it is not a leap year
        else:
            print(f"{year_entered} is not a leap year.")
    #If not divisible by 4 it is not a leap year
    else:
        print(f"{year_entered} is not a leap year.")


#Exit Prompt
input("Press [enter] to exit: ")