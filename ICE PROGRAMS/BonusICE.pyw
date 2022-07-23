#Martin Barber - 100368442
#Dec 8th, 2021
#Bonus 4 - L

from tkinter import * # Imports all widgets from tkinter
from tkinter.ttk import * # Windows 10 look

# CONSTANTS
HST = 1.13

# functions
def calculate_click():
    """
    Executed when the calculate button is clicked
    * Add 13% HST to the dollar amount
    """
    #Get the text from the input entry
    input_value = input_text.get() # Needs the get method to get the value of variable
    #Remove the $ before converting number
    input_value = input_value.replace("$","")

    #numeric validation, checking if its a float number because it can have decimals
    try:
        input_value = float(input_value)
        numeric = True
    except:
        numeric = False


    # Not Valid when not numeric
    if not numeric or input_value < 0:
        # Display Error
        output_text.set("Error - Invalid dollar amount!") #Setter method will se tthe value of the variable
        
    # Valid number
    else:
        # Calculate the output
        total_cost = input_value * HST
        # Display the Result
        input_text.set(f"${input_value:.2f}") #.2f means float number with 2 decimal places
        output_text.set(f"${total_cost:.2f}") #.2f means float number with 2 decimal places
        
def clear_click():
    """
    Clears the 2 input entries from anything written in them
    * Will reset input and output
    """
    input_text.set("$0.00")
    output_text.set("$0.00")

#activate the enter key and escape key to calculate and clear the screen
def key_handler(event:Event):
    """
    Function that handles key presses
    * Will calculate when user presses [enter]
    * Will clear when user presses [escape]
    """
    if event.keysym == "Escape":
        clear_click()
    elif event.keysym == "Return": # Return means Enter
        calculate_click()



# Setup the window
window = Tk()                                   # Create the TK window
window.title("HST Calcuator - Martin Barber")   # Set the Title
window.iconbitmap("Money.ico")                  # Set the Icon
window.resizable(width=False, height=False)     # Make window not resizeable
window.bind("<Key>", key_handler) #<Key> whenever a key is pressed, it will execute a function
 
# Add the Frame
frame = Frame()

# Labels
input_label = Label(frame, text="Enter Dollar amount: ")
output_label = Label(frame, text="Amount + HST: ")

# Entries
input_text = Variable()                                  # A tkinter variable for interface
input_text.set("$0.00")
input_entry = Entry(frame, width=60, textvariable=input_text)                   # Width = how many characters it can fit
                                                                                # textvariable stores what ever is in text box as variable
output_text = Variable()
output_text.set("$0.00")
output_entry = Entry(frame, width=60, state="readonly", textvariable=output_text)  # Readonly means we cant type in it

#Buttons
clear_button = Button(frame, text="Clear", command=clear_click)
calculate_button = Button(frame, text="Calculate", command=calculate_click)

# Position the frames (pack the fames)
frame.pack(padx=10, pady=10)                    # Adds padding of 10 pixels
input_label.pack(anchor="w")                    # Anchor sets where the test will end up
input_entry.pack()
output_label.pack(anchor="w")                   # Anchor sets where the test will end up "w" = West
output_entry.pack()
clear_button.pack(side="right", pady=(3,0))
calculate_button.pack(side="left",pady=(3,0))

# Draw the Window and make is visible
window.mainloop()