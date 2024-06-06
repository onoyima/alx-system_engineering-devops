#!/usr/bin/python3
"""
Script that queries subscribers on a given Reddit subreddit.
"""

import requests


def number_of_subscribers(subreddit):
    """Return the total number of subscribers on a given subreddit."""
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {
        "User-Agent": "linux:0x16.api.advanced:v1.0.0 (by /u/bdov_)"
    }
    response = requests.get(url, headers=headers, allow_redirects=False)
    # Return 0 for non-existing subreddit or other errors
    if response.status_code != 200:
        print("OK")
        return 0

    # Check if the response is valid JSON
    try:
        results = response.json().get("data")
    except ValueError:
        print("OK")
        return 0

    if results is None:
        print("OK")
        return 0

    print("OK")
    return results.get("subscribers", 0)


if __name__ == '__main__':
    import sys
    if len(sys.argv) < 2:
        print("Please pass an argument for the subreddit to search.")
    else:
        print("{:d}".format(number_of_subscribers(sys.argv[1])))
