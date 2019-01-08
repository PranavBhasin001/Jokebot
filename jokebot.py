"""Executes the Jokebot"""

from jokebot_utils import *
from jokebot_reddit_extractor import *
import sys


##########
# Jokebot
##########

# Functions

def main():
    """Encapsulation of the execution of the program"""
    # Assert statement to ensure that a joke file is provided in the command line args
    filepath = sys.argv[1:]
    jokebot_list = list()

    if len(filepath) > 1:
        jokebot_list = csv_jokebot_list(filepath[1])
    else:
        jokebot_list = reddit_jokebot_list()

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


def csv_jokebot_list(filepath):
    """Returns a list of jokes from the given file path, given the csv is provided for joke source"""

    # Asserting that the file is not empty
    jokebot_list = read_csv_file(filepath)
    assert jokebot_list, "No jokes found in the file"

    return jokebot_list


def reddit_jokebot_list():
    """Returns a list of jokes from reddit page: 'https://www.reddit.com/r/dadjokes.json'"""
    return json_to_list(request_page_json("https://www.reddit.com/r/dadjokes.json"))


# Execution of the Jokebot


main()
