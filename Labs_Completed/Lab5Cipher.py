#Martin Barber - 100368442
#Dec 3rd, 2021
#Lab 5 - Caesar Cipher
#Encrypts a secret message and decrypts a secret message

#input from system to use system  codes
from os import system
from colorama import Fore

#set console title
system("title Lab 5 Caesar Cypher - Martin Barber")

#CONSTANTS
INTRO = """===================
== Caesar Cipher ==
===================
"""
OPTION = """Choose an option:
1. Encrypt a message
2. Decrypt a message
3. Quit app
"""
ENCRYPTION_KEY = 2

def encrypt_data():
    """
    This will encrypt the data using the encryption formula
    """
    # START ENCRYPTING THE MESSAGE
    # This is the secret message you want to encrypt 
    message = input("Please type in the word / words you would like to Encrypt: ")
    # Starts empty, we will add encrypted letters 1 by 1 in the for loop 
    encrypted_message = "" 
    # Goes through each letter in the message 
    for letter in message: 
        # Encrypt the letter by getting its numeric value and adding the ENCRYPTION_KEY 
        encrypted_message += chr(ord(letter) + ENCRYPTION_KEY) 
    # Print the encrypted message 
    print(f"Encrypted message: {encrypted_message}\n")

def decrypt_data():
    """
    This will decrypt the information type into the input from the encryption formula
    """
    # START DECRYPTING THE MESSAGE
    # This is the secret message you want to encrypt 
    message = input("Please type in the word / words you would like to decrypt: ")
    # Starts empty, we will add encrypted letters 1 by 1 in the for loop 
    encrypted_message = "" 
    # Goes through each letter in the message 
    for letter in message: 
        # Encrypt the letter by getting its numeric value and adding the ENCRYPTION_KEY 
        encrypted_message += chr(ord(letter) - ENCRYPTION_KEY) 
    # Print the encrypted message 
    print(f"Decrypted Message: {encrypted_message}\n")

print(INTRO)
print("This app will Encrypt/decrypt a secret message using the Caesar Cipher.\n")
print(OPTION)
#Sets choice to false to enter while loop
choice = False

#Start the while loop incase there is an incorrect input
while choice != True:
    #Asking for the input for option
    selection = input("--> ")

    if selection == "1":
        #Sets choice to true to end the while loop
        choice = True
        # Pull the function encrypt_data 
        encrypt_data()

    elif selection == "2":
        #Sets choice to true to end the while loop
        choice = True
        # Pull the function encrypt_data 
        decrypt_data()
        

    elif selection == "3":
        #Sets choice to true to end the while loop Gsfe!Tujfcmfs
        choice = True
        #Exit the app
        exit()

    else:
        #Sets choice to False to continue the while loop
        choice = False
        print("Error - Invalid option")


#Exit Prompt
input("Press [enter] to exit: ")