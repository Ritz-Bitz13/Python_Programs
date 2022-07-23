#Martin Barber - 100368442
#Dec 8th, 2021
#BONUS ICE -  To do List
#Make a to do list where you can add and remove items on your list

from tkinter import *           # Imports all widgets from tkinter
from tkinter.ttk import *       # Windows 10 look
from tkinter import messagebox

CONVERT_TO_CEL = "Convert to Celcius"
CONVERT_TO_FAH = "Convert to Fahrenheit"


# Setup the window
window = Tk()                                   # Create the TK window
window.title("Temperature Calculations - Martin Barber")                # Set the Title
window.iconbitmap("Tasks.ico")                  # Set the Icon
window.minsize(width=350, height= 300)
window.resizable(width=False, height=False)   # Make window not resizeable

# Frames
input_frame = Frame()
radiobutton_frame = LabelFrame(text= "Please select what way you would like to convert:")
output_frame = Frame()

# Labels
enter_temperature_label = Label(input_frame, text="Please enter the temperature you want to convert:")
final_result_label = Label(output_frame, text="Converted Temperature:")

#Variable in Radio Button
convert_type = Variable()
# Radio Buttons
cel_to_fah = Radiobutton(radiobutton_frame, text=CONVERT_TO_FAH,variable=convert_type, value=CONVERT_TO_FAH)
fah_to_cel = Radiobutton(radiobutton_frame, text=CONVERT_TO_CEL,variable=convert_type, value= CONVERT_TO_CEL)

# Entrys
input_temperature = Variable()
temperature_input = Entry(input_frame, textvariable=input_temperature)
output_temperature = Variable()
converted_temperature = Entry(output_frame, state="readonly", textvariable=output_temperature)

# Buttons

# unpack items
    #input_frame unpacking
input_frame.pack(fill= "x", padx=10, pady=20)
enter_temperature_label.pack(anchor="w", fill="x")
temperature_input.pack(anchor="w")
    #radiobutton_frame unpacking
radiobutton_frame.pack(fill = "x", padx=10,pady=30)
cel_to_fah.pack(side="left")
fah_to_cel.pack(side= "right")

    #output_frame unpacking
output_frame.pack(fill="x", pady=20)
final_result_label.pack(anchor="w")
converted_temperature.pack(anchor="w", fill="x")


# Draw the Window and make is visible
window.mainloop()