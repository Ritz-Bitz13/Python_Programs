#Martin Barber - 100368442
#Dec 1st, 2021
#ICE 13 - Feedback Survey Questions
#Asks 3 Questions and once you submit a new window pops up revealing answers

from tkinter import *           #Imports all widgets from tkinter
from tkinter.ttk import *       #Windows 10 look
from tkinter import messagebox  #Imports messagebox

#CONSTANTS
#Question 1, question and answers
QUESTION_1 = "How satisfied are you with our company?"
ANSWER_Q1_A1 = "Satisfied"
ANSWER_Q1_A2 = "Neutral"
ANSWER_Q1_A3 = "Dissatisfied"

#Question 2, question and answers
QUESTION_2 = "How well do our products meet your needs?"
ANSWER_Q2_A1 = "Very Well"
ANSWER_Q2_A2 = "Somewhat"
ANSWER_Q2_A3 = "Not at all"

#Question 3, question and answers
QUESTION_3 = "Would you recommend our products to friends?"
ANSWER_Q3_A1 = "Definetly!"
ANSWER_Q3_A2 = "Not sure"
ANSWER_Q3_A3 = "Surely...NOT!"

# Functions
def submit_click():
    """
    Executed when the submit button is clicked
    * Shows an error pop-up when a question is left unanswered
    * Show a report pop-up when all questions are answered
    """

    # Incase the answer is empty
    if answer_q1.get() == "" or answer_q2.get() == "" or answer_q3.get() == "":
        messagebox.showwarning("Warning!", "Please answer all questions!")
    
    #answered all questions
    else:
        #format the report
        report = f"""
        {QUESTION_1}
        - {answer_q1.get()}

        {QUESTION_2}
        - {answer_q2.get()}

        {QUESTION_3}
        - {answer_q3.get()}
        """
        #display the report in a popup
        messagebox.showinfo("Report", report)

        #reset all answers to unchecked
        answer_q1.set("")           #Set value to empty string
        answer_q2.set("")           #Set value to empty string
        answer_q3.set("")           #Set value to empty string


# Setup the window
window = Tk()                                               #Create the TK window
window.title("Feedback Survey Questions - Martin Barber")   #Set the Title
window.iconbitmap("help.ico")                               #Set the Icon
window.resizable(width=False, height=False)                 #Make window not resizeable

# 3 Label frames for the questions
Q1_frame = LabelFrame(text = QUESTION_1)
Q2_frame = LabelFrame(text = QUESTION_2)
Q3_frame = LabelFrame(text = QUESTION_3)
extraframe = Frame()

######## QUESTION 1 ###########
# Add the Radio Buttons for Question 1
answer_q1 = Variable()      #Variable used in the radio buttons
#    button                       frame       text in button        link variable         set the variable value
q1_a1_radiobutton = Radiobutton(Q1_frame, text = ANSWER_Q1_A1, variable = answer_q1, value = ANSWER_Q1_A1)
q1_a2_radiobutton = Radiobutton(Q1_frame, text = ANSWER_Q1_A2, variable = answer_q1, value = ANSWER_Q1_A2)
q1_a3_radiobutton = Radiobutton(Q1_frame, text = ANSWER_Q1_A3, variable = answer_q1, value = ANSWER_Q1_A3)

######## QUESTION 2 ###########
answer_q2 = Variable()      #Variable used in the radio buttons
#    button                       frame       text in button        link variable         set the variable value
q2_a1_radiobutton = Radiobutton(Q2_frame, text = ANSWER_Q2_A1, variable = answer_q2, value = ANSWER_Q2_A1)
q2_a2_radiobutton = Radiobutton(Q2_frame, text = ANSWER_Q2_A2, variable = answer_q2, value = ANSWER_Q2_A2)
q2_a3_radiobutton = Radiobutton(Q2_frame, text = ANSWER_Q2_A3, variable = answer_q2, value = ANSWER_Q2_A3)

######## QUESTION 3 ########### 
answer_q3 = Variable()      #Variable used in the radio buttons
#    button                       frame       text in button        link variable         set the variable value
q3_a1_radiobutton = Radiobutton(Q3_frame, text = ANSWER_Q3_A1, variable = answer_q3, value = ANSWER_Q3_A1)
q3_a2_radiobutton = Radiobutton(Q3_frame, text = ANSWER_Q3_A2, variable = answer_q3, value = ANSWER_Q3_A2)
q3_a3_radiobutton = Radiobutton(Q3_frame, text = ANSWER_Q3_A3, variable = answer_q3, value = ANSWER_Q3_A3)

#Add button to submit answers
submit_button = Button(text = "Submit Answers", command=submit_click)

setting = Variable()
e = Entry(extraframe,width=60, textvariable=setting, state="readonly")
setting.set("Hello")



# Position the frames (pack the frames)
Q1_frame.pack(fill = "x", padx = 10, pady = 5)           # x = Fills the Horizontal Space
Q2_frame.pack(fill = "x", padx = 10, pady = 5)
Q3_frame.pack(fill = "x", padx = 10, pady = 5)

q1_a1_radiobutton.pack(anchor="w")
q1_a2_radiobutton.pack(anchor="w")
q1_a3_radiobutton.pack(anchor="w")

q2_a1_radiobutton.pack(anchor="w")
q2_a2_radiobutton.pack(anchor="w")
q2_a3_radiobutton.pack(anchor="w")

q3_a1_radiobutton.pack(anchor="w")
q3_a2_radiobutton.pack(anchor="w")
q3_a3_radiobutton.pack(anchor="w")

extraframe.pack()
e.pack(anchor="w")

submit_button.pack(pady = (5,10))                       # 5 padding at top, 10 padding at bottom


# Draw the Window and make is visible
window.mainloop()