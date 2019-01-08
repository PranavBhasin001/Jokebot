"""Functions and main for Jokebot"""
import time
import csv
import sys
import reddit_extractor.py


##########
# Jokebot
##########

def print_jokes(joke_prompt, joke_punchline):
    """Prints the joke prompt and joke punchline for a given joke"""
    print(joke_prompt)
    time.sleep(2)
    print(joke_punchline)
    return


def user_input():
    """Returns True value if the user inputs 'next',
    False value if the user inputs 'quit', and
    reruns with an error message in the case of any other input"""

    # Collects the user's input to determine return value
    jokebot_user_input = input("Would you like to hear a joke?(next/quit)")

    if jokebot_user_input == "next":
        return True
    elif jokebot_user_input == "quit":
        return False
    else:
        print("This Jokebot only knows how to tell another joke or quit")
        return user_input()


def read_csv_file(filepath):
    """Returns a list of prompt-punchline joke lists extracted
    from given csv file
    @source: https://realpython.com/python-csv/"""

    # Instantiating an empty list for storing values
    joke_list = list()

    # Opening csv through csv reader, with rows delimited by ','
    with open(filepath) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')

        # Append a list of row to the joke_list
        for row in csv_reader:
            joke_list.append(list(row))
    return joke_list


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


main()
