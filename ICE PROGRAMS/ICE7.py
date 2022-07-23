#Martin Barber - 100368442
#Oct 13th, 2021
#ICE 7 - Factorial
# App that calculates the Factorial of a number

#input from system to use system codes
from os import system

#set console title
system("title Ice7: Factorial - Martin Barber")

#Set the max number to be 20
MIN_NUMBER, MAX_NUMBER = 0, 20

#Validation loop
valid = False

print("========================")
print("= Factorial calculator =")
print("========================")
print("")

#Validation loop
while valid == False:
    number = input(f"Please enter a number between {MIN_NUMBER} and {MAX_NUMBER}: ")

    #make sure the number is between the range of Min and Max
    try:
        #Try to convert from string to integer
        number = int(number)#Converting
        numeric = True

    except:
        numeric = False

    #incase number is not number
    if numeric == False:
        print(f"ERROR - Please enter a numeric number")


    #incase number is not between 0 and 20
    elif number < MIN_NUMBER or number > MAX_NUMBER:
        print(f"Error - The number is not between {MIN_NUMBER} and {MAX_NUMBER}")

    #We got a valid number
    #Break the Loop asking to enter the number
    else:
        valid = True

#Calculate Factorial
output = 1
#count backwards from the input to 1 to MIN
for count in range(number,1, -1): #First number is the number given from user, second is where you're counting to, third is saying how you count to the number
    output = count*output
print(f"{number}!= {output}")

#Exit Prompt
input("Press [enter] to exit: ")