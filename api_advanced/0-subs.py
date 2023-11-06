#!/usr/bin/python3
"""

Write a function that queries the Reddit API
https://www.reddit.com/dev/api/
and returns the number of subscribers
(not active users, total subscribers) for a
given subreddit. If an invalid subreddit is given,
the function should return 0.

Hint: No authentication is necessary for most features
of the Reddit API. If you’re getting errors related to
Too Many Requests, ensure you’re setting a custom User-Agent.

"""


def number_of_subscribers(subreddit):
    import json
    import urllib.error
    import urllib.parse
    import urllib.request
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
