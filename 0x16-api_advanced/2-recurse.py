#!/usr/bin/python3
""" Function to query a list of all hot posts on a given Reddit subreddit."""

import requests


def recurse(subreddit, hot_list=[], after=None):
    """
    Recursively retrieves a list of titles of all hot posts
    on a given subreddit.

    Args:
        subreddit (str): The name of the subreddit.
        hot_list (list, optional): List to store the post titles.
                                   Default is an empty list.
        after (str, optional): Token used for pagination.
                               Default is None.

    Returns:
        list: A list of post titles from the hot section of the subreddit,
              or None if the subreddit is invalid.
    """
    # Construct the URL for the subreddit's hot posts in JSON format
    url = "https://www.reddit.com/r/{}/hot/.json".format(subreddit)

    # Define headers for the HTTP request, including User-Agent
    headers = {
        "User-Agent": "linux:0x16.api.advanced:v1.0.0 (by /u/bdov_)"
    }

    # Define parameters for the request, including pagination and limit
    params = {
        "after": after,
        "limit": 100
    }

    # Send a GET request to the subreddit's hot posts page
    response = requests.get(url, headers=headers, params=params,
                            allow_redirects=False)

    # Check if the response status code indicates a not-found error (404)
    if response.status_code == 404:
        return None

    # Parse the JSON response and extract relevant data
    try:
        results = response.json().get("data")
    except ValueError:
        return None

    if results is None:
        return None

    # Append post titles to the hot_list
    for child in results.get("children", []):
        hot_list.append(child.get("data", {}).get("title"))

    # Get the 'after' value for pagination
    after = results.get("after")

    # If there are more posts to retrieve, recursively call the function
    if after is not None:
        return recurse(subreddit, hot_list, after)

    # Return the final list of hot post titles
    return hot_list
