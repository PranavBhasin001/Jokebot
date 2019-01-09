"""Executes the Jokebot"""

from jokebot_utils import *
import sys

##########
# Jokebot
##########

# Variables

reddit_url = "https://www.reddit.com/r/dadjokes.json"


# Functions

def main():
    """Executes the program"""
    # Assert statement to ensure that a joke file is provided in the command line args
    filepath = sys.argv[1:]
    source_mode_reddit = select_source_mode(filepath)
    jokebot_list = reddit_jokebot_list(reddit_url) if source_mode_reddit & url_validation(reddit_url) \
        else csv_jokebot_list(filepath[1])
    curr_mode = "Reddit" if source_mode_reddit else "the CSV File"
    print("Your jokes are coming hot right out of", curr_mode, "any second!")

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
