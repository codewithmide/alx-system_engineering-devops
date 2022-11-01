#!/usr/bin/python3
"""
Write a function that queries the Reddit API and prints the titles of the first 10 hot posts listed for a given subreddit.

Requirements:

If not a valid subreddit, print None.
NOTE: Invalid subreddits may return a redirect to search results. Ensure that you are not following redirects.
"""
import requests
import json


def top_ten(subreddit):
    """
    If not a valid subreddit, print None.
    """
    url = "https://www.reddit.com/r/{}/hot/.json".format(subreddit)
    headers = {
        "User-Agent": "User Agent"
    }
    params = {
        "limit": 10
    }
    response = requests.get(url, headers=headers, params=params,
                            allow_redirects=False)
    if response.status_code != 404:
        results = response.json().get("data")
        [print(c.get("data").get("title")) for c in results.get("children")]
    else:
        return print("None")