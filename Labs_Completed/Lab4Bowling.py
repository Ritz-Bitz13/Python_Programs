#Martin Barber - 100368442
#Nov 17th, 2021
#Lab 4 - Bowling Scores
#

#input from system to use system  codes
from os import system
from colorama import Fore

#CONSTANTS
LIST_LENGTH = 6

#Variables
restart = "y"

#set console title
system("title Lab 4: Bowling Scores - Martin Barber")

#Create an empty list with a capacity for 5 elements
bowler_list = [None] * LIST_LENGTH

#Starting the app keeping everything in a loop incase the user wants to enter more scores
while restart == "y":
    system("cls")
    final_average = 0 #Set average to 0
    index = 0 #Start at index 0
    

    while index != LIST_LENGTH:
        #Ask for a number
        bowling_score = input(f"Enter the score you recieved for bowler #{index + 1}: ")

        #Check if input is numeric
        try:
            bowling_score = int(bowling_score)
            numeric = True
        except:
            numeric = False

        #Incase input is not numeric
        if not numeric:
            print(Fore.LIGHTRED_EX + "Error - Number is not numeric" + Fore.RESET)
        elif bowling_score < 1 or bowling_score > 300:
            print(Fore.LIGHTRED_EX + "Please enter a score between 1 and 300." + Fore.RESET)

        #Only increases the index, if input is numeric
        #Incase number is numeric
        else:
            #Add number to the list
            bowler_list[index] = bowling_score
            #Adding all the scores together to eventually calculate the average after
            final_average = bowling_score + final_average
            index += 1 #Go to next index

    #NOTE DOES NOT REACH HERE UNTIL 6 SCORES HAVE BEEN ENTERED!

    #Getting the average of the scores
    final_average = final_average / LIST_LENGTH
    final_average = int(final_average)




    ########################### SHOWING THE SCORES ##########################################
    system("cls")
    print("==========================================================")
    print("                   Bowling Game Scores                    ")             
    print("----------------------------------------------------------")
    print(f"B1: {bowler_list[0]}    B2: {bowler_list[1]}    B3: {bowler_list[2]}    B4: {bowler_list[3]}    B5: {bowler_list[4]}    B6: {bowler_list[5]}")
    print("----------------------------------------------------------")


    ##################################################################################################################
    #####################################  Find the highest score  ###################################################
    ##################################################################################################################

    #Reset highest score to reset the tests
    highest_score = 0

    #Check the list for the highest score
    for high in range(0, LIST_LENGTH-1):
        #Checks the first number on the list with the second, If second number is higher
        if bowler_list[high] > bowler_list[high+1] and bowler_list[high] >= highest_score:
            highest_score = bowler_list[high]
            bowler_number = high
    
    #Because the check doesnt fully check the last number on the list. This will check if the highest score found above is higher than the last number on the list
    if highest_score < bowler_list[LIST_LENGTH-1]:
        highest_score = bowler_list[LIST_LENGTH-1]
        bowler_number = LIST_LENGTH-1


    ##################################################################################################################
    ##########################################  Find the Lowest Score  ###############################################
    ##################################################################################################################

    #Reset lowest score to reset tests incase app restarted
    lowest_score = 300

    #Check the list for the lowest score
    for low in range(0, LIST_LENGTH-1):
        #Checks the first number on the list with the second, If second number is higher
        if bowler_list[low] < bowler_list[low+1] and bowler_list[low] <= lowest_score:
            lowest_score = bowler_list[low]
            bowler_number_low = low

    #Because the check doesnt fully check the last number on the list. This will check if the lowest score found above is lower than the last number on the list
    if lowest_score > bowler_list[LIST_LENGTH-1]:
        lowest_score = bowler_list[LIST_LENGTH-1]
        bowler_number_low = LIST_LENGTH-1


    print(f"Bowler #{bowler_number+1} had the highest score with a score of: {highest_score}")
    print(f"Bowler #{bowler_number_low+1} had the lowest score with a score of: {lowest_score}") 
    print(f"Average score in this game is {final_average} points")
    print("==========================================================")




#Exit Prompt    
    restart = input("\nPress [y] to enter new scores or hit [enter] to exit: ").lower()
    index = 0 #Start at index 0