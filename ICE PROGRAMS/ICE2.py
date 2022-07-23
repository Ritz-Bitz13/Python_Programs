#Martin Barber - 100368442
#Sept 20th, 2021
#ICE 2 - Even odd number
# See if a number is Even or Odd

#input from system to use system  codes
from os import system

#set console title
system("title Even odd number - Martin Barber")

#Ask user to input a whole number
entered_number = input("Please enter a whole number: ")

#Try to convert to and integer
try:
    entered_number = int(entered_number)
    numeric = True #able to convert
except:
    numeric = False #unable to convert

#If the entered item is not a number it will come back saying this is not a number
if not numeric:
    print("Error! Invalid Input!")
else:
    #Check if number is divisible by 2
    remainder = entered_number % 2

    #Deciding if number entered is even or odd
    if remainder == 0:
        print("Your number " + str(entered_number) + " is EVEN!")
    else:
        print("Your number " + str(entered_number)  + " is ODD!")


#Press enter to end the program
input("Press ENTER to exit: ")


#COPY FROM HERE!!!!!!!!!!!!!!!!!!!!!
#Martin Barber - 100368442
#Nov 26th, 2021
#BONUS ICE - HST Calculator 
#Calculates the HST tax

from tkinter import * #Imports all widgets from tkinter
from tkinter.ttk import * #Windows 10 look
from tkinter import messagebox

# Setup the window
window = Tk()                                   #Create the TK window
window.title("HST Calcuator - Martin Barber")   #Set the Title
window.iconbitmap("Money.ico")                  #Set the Icon
window.resizable(width=False, height=False)     #Make window not resizeable

# Add the Frame
frame = Frame()

# Labels

# Position the frames (pack the fames)
frame.pack(padx=10, pady=10)                    #Adds padding of 10 pixels


# Draw the Window and make is visible
window.mainloop()