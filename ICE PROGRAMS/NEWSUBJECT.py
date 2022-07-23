#Functions only execute when called
#parameters (var) only exist within the function

def greet(name:str):
    """
    This fuction will greet the user with a friendly hello!
    """
    print(f"Hello {name}!")

#calling the function
greet("Fred")


def exit_prompt():
    """
    Asks the user to press ENTER to exit
    """
    input("Press [enter] to exit: ")

def multiply(number1:int, number2:int):
    """
    This function multiplies two numbers
    """
    #No need to calculate if answer is 0
    if number1 == 0 or number2 == 0: return 0
    #multiply the numbers
    return number1 * number2

############################################
result = multiply(2, 11)
print(result)
#means the same:     print(multiply(2,11))
############################################


exit_prompt()