#Martin Barber - 100368442
#Dec 8th, 2021
#BONUS ICE -  To do List
#Make a to do list where you can add and remove items on your list

from tkinter import *           # Imports all widgets from tkinter
import random
import math

#CONSTANTS
CANVAS_WIDTH, CANVAS_HEIGHT = 640, 480
CANVAS_CENTER_X, CANVAS_CENTER_Y = CANVAS_WIDTH/2, CANVAS_HEIGHT/2
DOUGH_RADIUS = 200
CHEESE_RADIUS = 180
PEPERONI_RADIUS = 20
PEPERONI_COUNT = 30

def create_circle(radius:float, center_x:float, center_y:float, fill_colour:str):
    """
    Draw a circle center at the given x, y coordinates
    """
    #calculate the corners
    x1, x2 = center_x - radius, center_x + radius
    y1, y2 = center_y - radius, center_y + radius

    #draw circle
    canvas.create_oval(x1,y1, x2,y2, fill=fill_colour)



#Setup Window
window = Tk()                                                  # Create the TK window
window.title("Pizza Generator - Martin Barber")                # Set the Title
window.iconbitmap("art.ico")                                   # Set the Icon
window.resizable(width=False, height=False)                    # Make window not resizeable

#Create Canvas
canvas = Canvas(width = CANVAS_WIDTH, height = CANVAS_HEIGHT, background="white")

#drawing the dough
create_circle(DOUGH_RADIUS,CANVAS_CENTER_X,CANVAS_CENTER_Y, "wheat")
#Drawing the cheese
create_circle(CHEESE_RADIUS,CANVAS_CENTER_X,CANVAS_CENTER_Y, "yellow")

#Place many pepperoni
for count in range(PEPERONI_COUNT):
    #validates is pepperoni is on top of the cheese
    valid = False
    while not valid:
    #pepperoni position
        position_x = CANVAS_CENTER_X + random.randint(-CHEESE_RADIUS, CHEESE_RADIUS)
        position_y = CANVAS_CENTER_Y + random.randint(-CHEESE_RADIUS, CHEESE_RADIUS)
        #Check the distance between pepperoni and the cheese
        valid = math.dist((position_x,position_y), (CANVAS_CENTER_X,CANVAS_CENTER_Y)) <CHEESE_RADIUS - PEPERONI_RADIUS
#Drawing the pepperoni
    create_circle(PEPERONI_RADIUS, position_x, position_y, "red4")


#Place the canvas with pack()
canvas.pack()

# Draw the Window and make is visible
window.mainloop()