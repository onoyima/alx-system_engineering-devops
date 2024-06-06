#!/usr/bin/python3
"""
Scripts to print hot posts on a given Reddit subreddit.
"""
import requests


def top_ten(subreddit):
    """Print the titles of the 10 hottest posts on a given subreddit."""
    # Construct the URL for the subreddit's hot posts in JSON format
    url = "https://www.reddit.com/r/{}/hot/.json".format(subreddit)

    # Define headers for the HTTP request, including User-Agent
    headers = {
        "User-Agent": "linux:0x16.api.advanced:v1.0.0 (by /u/bdov_)"
    }

    # Define parameters for the request, limiting the number of posts to 10
    params = {
        "limit": 10
    }

    # Send a GET request to the subreddit's hot posts page
    response = requests.get(url, headers=headers, params=params, allow_redirects=False)

    # Check if the response status code indicates a not-found error (404)
    if response.status_code != 200:
        print("None")
        return

    # Check if the response is valid JSON
    try:
        results = response.json().get("data")
    except ValueError:
        print("None")
        return

    if results is None:
        print("None")
        return

    # Print the titles of the top 10 hottest posts
    for child in results.get("children", []):
        print(child.get("data", {}).get("title"))

if __name__ == '__main__':
    import sys
    if len(sys.argv) < 2:
        print("Please pass an argument for the subreddit to search.")
    else:
        top_ten(sys.argv[1])
