#Martin Barber - 100368442
#Sept 23rd, 2021
#Lab 1 - BMI Calculator
#This lab will calculate what the BMI is for a person with their height and weight.

#input from system to use system  codes
from os import system

#set console title
system("title BMI Calculator - Martin Barber")

#Constants used in this program
FEET_TO_INCHES = 12
BMI_RATIO_MASS = 703

#Starting Code
#Getting the user to input their height and weight in
height = input("Please enter your height in feet and inches: ")
weight = input("Please enter the persons weight in pounds: ")

#Test to see if both numbers are integers
#I know you said we dont have to verify but I like making sure they're proper
try:
    feet_person, inches_person = height.split()
    feet_person = int(feet_person)
    inches_person = float(inches_person)
    weight = float(weight)
    #Set weight to 1 decimal place
    weight = round(weight, 1)

    #if worked then valid = True
    valid = True

    #If numbers are valid continue with the calculation
    #First calculate total inches and round to a tenth decimal place (aka 1 decimal place)
    total_inches = feet_person * FEET_TO_INCHES + inches_person
    total_inches = float(total_inches)
    total_inches = round(total_inches, 1)


    #Calculate the total BMI of the person
    final_BMI = weight / (total_inches * total_inches) * BMI_RATIO_MASS
    final_BMI = float(final_BMI)
    #round to a tenth decmial place (aka 1 decimal place)
    final_BMI = round(final_BMI, 1)
except:
    #if input for height does not meet requirements then the valid = False
    valid = False


# If Valid = False if should respond with an incorrect statement
if not valid:
    print("Error, information entered incorrectly!")


#Checks final_BMI is 15.9 or less then print the result adding that the user is severly underweight!
elif final_BMI <= 15.9:
    print(f"The BMI for a {total_inches} inches tall person who weights {weight} lbs is {final_BMI}, which is concidered 'severely underweight!'")
#If final_BMI is beterrn 16 and 18.4 then print the result adding that the user is just underweight
elif final_BMI >= 16 and final_BMI <= 18.4:
    print(f"The BMI for a {total_inches} inches tall person who weights {weight} lbs is {final_BMI}, which is concidered 'underweight!'")
#If final_BMI is beterrn 18.5 and 24.9 then print the result adding that the user is healthy
elif final_BMI >= 18.5 and final_BMI <= 24.9:
    print(f"The BMI for a {total_inches} inches tall person who weights {weight} lbs is {final_BMI}, which is concidered 'healthy!'")
#If final_BMI is beterrn 25 and 29.9 then print the result adding that the user is overweight
elif final_BMI >= 25 and final_BMI <= 29.9:
    print(f"The BMI for a {total_inches} inches tall person who weights {weight} lbs is {final_BMI}, which is concidered 'overweight!'")
#If final_BMI is 30 or over then they are concidered obese 
elif final_BMI >= 30:
    print(f"The BMI for a {total_inches} inches tall person who weights {weight} lbs is {final_BMI}, which is concidered 'obese!'")


#Exit Prompt
input("Press <ENTER> to exit: ")