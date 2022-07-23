#Martin Barber - 100368442
#Nov 3rd, 2021
#ICE 9 - Palindrome
#Checks the word you type in, is a palindrome or not

#input from system to use system  codes
from os import system
from colorama import Fore

restart = "r"

#set console title
system("title Ice 9 Palindrome - Martin Barber")


while restart == "r":
    #Clear screen incase you restart it isnt flooded with text
    system("cls")
    #Prompt for a word / Phrase
    original_word = input("Enter a word or phrase: ")

    #Word copy
    word_copy = original_word.replace("?", "").replace(" ", "").lower()
    is_palindrome = True

    #Check if the word is palindrome
    #count up to half the word
    half_length = round(len(word_copy)/2) #Round so if u have an odd number of letters

    #count up to half the length of the word (rounded to an int)
    for count in range(half_length):
        #check if the first character are the same
        if word_copy[count] != word_copy[len(word_copy)-1-count]:
            is_palindrome = False
            break

    if is_palindrome == True:
        print(f"{original_word} is a palindrome")
    else:
        print(f"{original_word} is not a palindrome")


    #Exit Prompt    
    restart = input("Press [r] to restart: ").lower()