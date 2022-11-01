#!/usr/bin/python3
"""
Write a recursive function that queries the Reddit API
and returns a list containing the titles of all hot articles
for a given subreddit. If no results are found for the
given subreddit, the function should return None.

Hint: The Reddit API uses pagination for separating pages of responses.

Requirements:

Prototype: def recurse(subreddit, hot_list=[])
Note: You may change the prototype, but it must
be able to be called with just a subreddit supplied.
AKA you can add a counter, but it must work without
supplying a starting value in the main.

If not a valid subreddit, return None.
NOTE: Invalid subreddits may return a redirect to search results.
Ensure that you are not following redirects.

Your code will NOT pass if you are using a loop and not
recursively calling the function! This /can/ be done with a
loop but the point is to use a recursive function. :)
"""


def recurse(subreddit, hot_list=[], after=None, count=0):
    """
    queries the Reddit API
    returns list of titles of hot posts for subreddit
    """
    import json
    import requests
    if after is None:
        sub_URL = 'https://www.reddit.com/r/{}/hot.json'.format(subreddit)
    else:
        sub_URL = 'https://www.reddit.com/r/{}/hot.json?after={}'.format(
            subreddit, after)
    subreddit_info = requests.get(sub_URL,
                                  headers={"user-agent": "user"},
                                  allow_redirects=False).json()
    if "data" not in subreddit_info and hot_list == []:
        return None
    children = subreddit_info.get("data").get("children")
    for child in children:
        hot_list.append(child.get("data").get("title"))
        count += 1
    after = subreddit_info.get("data").get("after")
    if after is None:
        return hot_list
    return (recurse(subreddit, hot_list, after, count))
