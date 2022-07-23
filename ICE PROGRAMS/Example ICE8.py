#Martin Barber - 100368442
#Oct 20th, 2021
#ICE 8 Example - 
#

#CONSTANTS
TABLE_MIN = 1
TABLE_MAX = 10


#input from system to use system  codes
from os import system

#set console title
system("title Ice8 Example Multiplication tables:  - Martin Barber")

valid = False

while valid == False:
    #ask for 2 numbers
    start_stop = input("Enter 2 numbers: ")

    try:
        #Try to split and assign 2 variables
        start, stop = start_stop.split()
        #Try to convert to int
        start = int(start)
        stop = int(stop)
        #input is valid
        valid = True

    except:
        #everything is not good
        print("Error - Invalid Input")

#Print the multiplication tables
for multiplicand in range(start,stop+1):
    for multiplyer in range (TABLE_MIN, TABLE_MAX+1):
        result = multiplicand * multiplyer
        print(f"{multiplicand} x {multiplyer} = {result}")
    print("\n--------------------------------")


#Exit Prompt
input("Press [enter] to exit: ")