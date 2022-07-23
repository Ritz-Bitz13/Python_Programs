#Martin Barber - 100368442
#Dec 8th, 2021
#BONUS ICE -  To do List
#Make a to do list where you can add and remove items on your list

from tkinter import *           # Imports all widgets from tkinter
from tkinter.ttk import *       # Windows 10 look
from tkinter import messagebox



def add_item():
    """
    Adds a task to the list
    * If the entry is empty, show a warning!
    """

    new_task = add_item_text.get()

    if new_task == "":
        messagebox.showwarning("Warning!", "Please enter a task")

    # Text is not empty then add to the list!
    else:
        # add the new task to the data type list
        task_list.append(new_task)
        # update the GUI list
        listbox_items.set(task_list)
        # Reset entry
        add_item_text.set("")

def remove_task():
    """
    Remove the selected task from the list
    * Show a warning in case no item is selected
    """

    #nothing selected - current selection is empty
    if not listbox.curselection():
        messagebox.showwarning("Warning!", "Please select a task to remove!")
    
    #Selected a task
    else:
        #Get the test of the current selection
        selection = listbox.selection_get()
        #Remove the selected Item
        task_list.remove(selection)

        #update GUI list
        listbox_items.set(task_list)

################### KEYBOARD EVENT #############################

def key_handler(event:Event):
    """
    Handle Key presses
    """
    if event.keysym == "Delete":
        remove_task()
    elif event.keysym == "Return":      # Return is the enter key
        add_item()


################### KEYBOARD EVENT #############################

# Setup the window
window = Tk()                                   # Create the TK window
window.title("To do list - Martin Barber")                # Set the Title
window.iconbitmap("Tasks.ico")                  # Set the Icon
window.minsize(width=350, height= 300)
# window.resizable(width=False, height=False)   # Make window not resizeable

############## KEYBOARD SHORTCUTS
window.bind("<Key>", key_handler) #Whenever you type something, it will call a function


# Add the Frame
input_frame = Frame()
output_frame = Frame()

# Banner Label
banner_label = Label(output_frame, text="Task List", font="Areal 24", foreground="blue")

# ListBox
task_list = ["Walk dog", "Shovel The Driveway", "Play Halo Infinite", "Do homework"]                          # List of test Tasks
listbox_items = Variable()                                                                                    # Create a new Variable in widgets
listbox_items.set(task_list)
listbox = Listbox(output_frame, listvariable=listbox_items)

# New task Entry
add_item_text = Variable()    #holds the text from entry
add_item_entry = Entry(input_frame, textvariable=add_item_text)

# Buttons
add_button = Button(input_frame, text = "Add task",command = add_item)
remove_button = Button(input_frame, text = "Remove Selected Task", command=remove_task)

# Position the frames (pack the fames)
output_frame.pack(padx=10, pady=10, fill="both", expand = True)                         # padx / pady : Adds padding of 10 pixels
input_frame.pack(padx=(10), pady=(0,10),side="bottom", fill="x")      # Stuck to the bottom of the window with : side="bottom"
banner_label.pack()
listbox.pack(fill="both", expand = True)
add_item_entry.pack(side="left", fill="x",expand=True)                            # All to left means they are on the same line    ////   expand means occupy all space
add_button.pack(side="left", padx=3)
remove_button.pack(side="left")



# Draw the Window and make is visible
window.mainloop()