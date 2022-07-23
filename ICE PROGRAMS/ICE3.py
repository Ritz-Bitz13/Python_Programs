#Martin Barber - 100368442
#Sept 22nd, 2021
#ICE 3 - length converter
# This will convert cm to inches and vice versa

#input from system to use system codes
from os import system

#App Title
system("title ICE 3 - Martin Barber")

#Constant values that do not change
CONVERSION_FACTOR = 2.54

#Starting Code
#asking the user to enter a length and unit
starting = input("Please enter a length and unit: ")

try: 
    #Tries to split the input into 2 different variables
    measurement, unit = starting.split()
    # try to convert measurement into float
    measurement = float(measurement)

    #If true / worked
    valid = True
except:
    #If it did not work
    valid = False

#Write an error message if the valid is false or is not Valid
if not valid:
    #Add colour to error
    print("Error, not proper input")

#If the input is inches, convert to CM, vice versa
elif unit == "in" or unit == "inches":
    #Convert inches to centimeters
    output = measurement * CONVERSION_FACTOR
    #round to 2 decimal places and save the variable
    output = round(output, 2)

    #Write result
    print(f"{measurement} inches corrisponds to {output} cm")

#If the input is centimeters, convert to inches, vice versa
#5 cm
elif unit == "cm" or unit == "centimeters":
    #Convert inches to centimeters
    output = measurement / CONVERSION_FACTOR
    #round to 2 decimal places and save the variable
    output = round(output, 2)

    #Write result
    print(f"{measurement} centimeters corrisponds to {output} inches")

else:
    #Invalid Unit
    print("Invalid conversion unit ")

#Exit Prompt
input("Press ENTER to exit: ")