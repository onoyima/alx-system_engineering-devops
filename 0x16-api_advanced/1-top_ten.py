#!/usr/bin/python3
"""
Module to print the titles of the top 10 hot posts on a given Reddit subreddit.
"""

import requests


def top_ten(subreddit):
    """
    Print the titles of the 10 hottest posts on a given subreddit.
    Args:
        subreddit (str): The name of the subreddit.
    """
    url = "https://www.reddit.com/r/{}/hot/.json".format(subreddit)
    headers = {
        "User-Agent": "linux:0x16.api.advanced:v1.0.0 (by /u/bdov_)"
    }
    params = {
        "limit": 10
    }
    try:
        response = requests.get(url, headers=headers, params=params,
                                allow_redirects=False)
        if response.status_code == 404:
            print(None)
            return
        results = response.json().get("data", {}).get("children", [])
        if not results:
            print(None)
            return
        for post in results:
            print(post.get("data", {}).get("title"))
    except Exception:
        print(None)
