# dice.py


# create function 'parse_input()' with the argument set to the input string
def parse_input(input_string):
    # define docstring for the function
    """Return 'input_string' as integer between 1 and 6.

    Check if 'input_string' is an integer number between 1 and 6.
    If so, return an integer with the same value. Othewise, tell
    the user to enter a valid number and quit the program.
    """
    # create if-statement which will check that input is acceptable
    if input_string.strip() in {"1", "2", "3", "4", "5", "6"}:
        # return the input string as an integer, if it is validated
        return int(input_string)
    # create else-statement to handle invalid inputs
    else:
        # print string telling user to enter a valid number
        print("Please enter a number from 1 to 6.")
        # exits the app with 'SystemExit' exception and status code of 1 to show something went wrong
        raise SystemExit(1)



# ~~~ App's main code block ~~~
# 1. Get and validate the user's input

# define variable 'num_dice_input' which calls input() to collect 
# user input on the number of dice to roll, which must fall between
# 1 and 6, inclusively
num_dice_input = input("How many dice do you want to roll? [1-6] ")
# define variable 'num_dice' which calls function parse_input on
# variable 'num_dice_input' and stores the return value in 'num_dice'
num_dice = parse_input(num_dice_input)