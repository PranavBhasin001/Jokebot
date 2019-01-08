"""Functions reddit page jokes extraction"""

import requests

##########################
# Jokebot Reddit Extractor
##########################


def request_page_json(reddit_url):
    """"""
    r = requests.get(reddit_url, headers={'User-agent': 'your bot 0.1'})
    return r.json()


def json_to_list(json_object):
    """"""
    json_data = json_object['data']['children']
    joke_list = list()

    for joke_data in json_data:
        if check_interrogative(joke_data) & check_safe_for_work(joke_data):
            joke_item = [get_prompt(joke_data), get_punchline(joke_data)]
            joke_list.append(joke_item)

    return joke_list


def check_safe_for_work(joke_data):
    return False if joke_data["data"]["over_18"] else True


def check_interrogative(joke_data):
    """"""
    condition = get_prompt(joke_data).split(" ")[0] in ["How", "What", "Why"]
    return True if condition else False


def get_prompt(joke_data):
    """"""
    return joke_data["data"]["title"]


def get_punchline(joke_data):
    """"""
    return joke_data["data"]["selftext"]
