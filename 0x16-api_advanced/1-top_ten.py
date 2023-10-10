#!/usr/bin/python3
"""Query subreddit"""

import requests


def top_ten(subreddit):
    """Query Reddit and print titles of the first 10 hot posts"""
    url = f"https://www.reddit.com/r/{subreddit}/hot.json?limit=10"

    # Set a custom User-Agent to avoid too many requests error
    headers = {'User-Agent': 'My user Agent 1.0'}

    # send a GET request to the Reddit API
    response = requests.get(url, headers=headers, allow_redirects=False)

    # Chek if the request was successful and not redirect
    if response.status_code == 200 and not response.is_redirect:
        # Parse the JSON response and extract post titles
        children = response.json().get('data').get('children')
        for i in range(10):
            print(children[i].get('data').get('title'))
        else:
            print("None")
