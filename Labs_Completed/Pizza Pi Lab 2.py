#Martin Barber - 100368442
#Oct  6th, 2021
#Lab 2 - Pizza Pi 
#Once given the diameter of a pizza the customer would like, feed back how many slices the user will recieve and the area of the pizza!

#input from system to use system codes
from os import system

#Import math to use pie
import math

#set console title
system("title Lab 2: Pizza Pi - Martin Barber")

#CONSTANTS
SMALL = 12
MEDIUM = 14
LARGE = 16
EXTRA_LARGE = 20
WHOLE_PIZZA_ANGLE = 360

#Asking user to enter a diameter
diameter = input("Please enter the diameter of your pizza: ")

#Try to convert to integer
try:
    diameter = int(diameter)
    numeric = True #Able to convert
except:
    numeric = False #Unable to convert

#If number is not numeric
if not numeric:
    print(" Error Diameter must be Numeric!")

#If number is numeric but isnt within the ranges of 8 - 24 inches
elif diameter < 8 or diameter > 24:
    print("Error - Diameter must be in the range of 8 inches to 24 inches inclusive")

#Success Valid check
else:
    #Check Diameter for what size the pizza is to determine amount of slices
    if diameter < SMALL:
        slices = 6
    elif diameter >= SMALL and diameter < MEDIUM:
        slices = 8
    elif diameter >= MEDIUM and diameter < LARGE:
        slices = 10
    elif diameter >= LARGE and diameter < EXTRA_LARGE:
        slices = 12
    elif diameter >= EXTRA_LARGE:
        slices = 16
    
    #Start calculations for the extra information of area of Pizza
    #Find Radius
    radius = diameter / 2

    #Calculate area of pizza
    area_pizza = math.pi * radius * radius
    #Round the area of the pizza to 2 decimal places
    area_pizza = round(area_pizza, 2)

    #Claculate each slice area
    slice_area = area_pizza / slices
    slice_area = round(slice_area, 2)

    #calculate degrees of slices
    cut_slice = WHOLE_PIZZA_ANGLE / slices

    print(f"A {diameter} Inch pizza has an area of {area_pizza} square inches and will yield, {slices} slices.")
    print(f"Each slice will be cut at {cut_slice} degrees and have an area of {slice_area} square inches.")

#Exit Prompt
input("Press [enter] to exit: ")