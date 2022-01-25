# dice.py

# ~~~ App's main code block ~~~
# 1. Get and validate the user's input

# define variable 'num_dice_input' which calls input() to collect 
# user input on the number of dice to roll, which must fall between
# 1 and 6, inclusively
num_dice_input = input("How many dice do you want to roll? [1-6] ")
# define variable 'num_dice' which calls function parse_input on
# variable 'num_dice_input' and stores the return value in 'num_dice'
num_dice = parse_input(num_dice_input)