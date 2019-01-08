"""Functions and main for Jokebot"""

from jokebot_utils import *
from jokebot_reddit_extractor import *
import sys


##########
# Jokebot
##########

# Functions

def main():
    """Function to enable IntelliJ Python runner feature"""
    # Assert statement to ensure that a joke file is provided in the command line args
    filepath = sys.argv[1:]
    assert filepath, "No jokes file found"

    # Asserting that the file is not empty
    jokebot_list = read_csv_file(filepath[1])
    assert jokebot_list, "No jokes found in the file"

    while True:

        response = user_input()

        if not jokebot_list:
            print("Jokebot is out of jokes!")
            break

        if response:
            curr_joke = jokebot_list.pop(0)
            print_jokes(curr_joke[0], curr_joke[1])

        else:
            print("Thank you for using the Jokebot")
            break

    return

# Execution of the Jokebot


main()
