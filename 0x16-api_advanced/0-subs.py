#!/usr/bin/python3
"""Quering Reddit"""

import requests


def number_of_subscribers(subreddit):
    """query a subreddit and retrive no of subscribers"""

    # Reddit API endpoint for getting subreddit informatiom
    url = 'http://www.reddit.com/r/{}/about.json'.format(subreddit)

    # Set a custom User-Agent to avoid too many requests error
    headers = {'User-Agent': 'My user Agent 1.0'}

    # send a GET request to the Reddit API
    response = requests.get(url, headers=headers, allow_redirects=False)

    # Chek if the request was successful and not redirect
    if response.status_code == 200 and not response.is_redirect:
        # parse JSON response to extract no of subscribers
        data = response.json()
        return data.get('data').get('subscribers')
    else:
        return 0
