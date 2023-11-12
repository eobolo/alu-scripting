#!/usr/bin/python3
"""Function to count words in all hot posts of a given Reddit subreddit."""
import json
import urllib.error
import urllib.parse
import urllib.request


def number_of_subscribers(subreddit):
    """Prints counts of given words found in hot posts of a given subreddit.

    Args:
        subreddit (str): The subreddit to search.
        word_list (list): The list of words to search for in post titles.
        instances (obj): Key/value pairs of words/counts.
        after (str): The parameter for the next page of the API results.
        count (int): The parameter of results matched thus far.
    """
    # create a url
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    # create a request object
    req_object = urllib.request.Request(url, method="GET")
    # create a custom user agent
    req_object.add_header('User-Agent', 'OboloScript/1.0')
    # open the url and send req_object to server and get
    # a response
    try:
        with urllib.request.urlopen(req_object) as res_object:
            res_json = json.JSONDecoder().decode(res_object.
                                                 read().decode("utf-8"))
    except urllib.error.HTTPError:
        return 0
    else:
        return res_json["data"]["subscribers"]
