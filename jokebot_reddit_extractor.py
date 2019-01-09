"""Functions reddit page jokes extraction"""

import requests


##########################
# Jokebot Reddit Extractor
##########################

# Functions


def request_page_json(reddit_url):
    """Requests page data in JSON format from the provided url"""
    r = requests.get(reddit_url, headers={'User-agent': 'jokebot_2.0'})
    return r.json()


def json_to_list(json_object):
    """Converts the provided JSON data into a list of lists containing prompt-punchline jokes
    that are safe for work and are interrogative in nature"""
    json_data = json_object['data']['children']
    joke_list = list()

    for joke_data in json_data:
        if check_interrogative(joke_data) & check_safe_for_work(joke_data):
            joke_item = [get_prompt(joke_data), get_punchline(joke_data)]
            joke_list.append(joke_item)

    return joke_list


def check_safe_for_work(joke_data):
    """Returns True if the joke data's over_18 parameter is False, else returns False"""
    return False if joke_data["data"]["over_18"] else True


def check_interrogative(joke_data):
    """Returns True if the joke's punchline starts with How, What or Why, else returns False"""
    condition = get_prompt(joke_data).split(" ")[0] in ["How", "What", "Why"]
    return True if condition else False


def get_prompt(joke_data):
    """Returns the prompt from joke_data"""
    return joke_data["data"]["title"]


def get_punchline(joke_data):
    """Returns the punchline associated with joke_data"""
    return joke_data["data"]["selftext"]
