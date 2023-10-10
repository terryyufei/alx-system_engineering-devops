#!/usr/bin/python3
"""Quering Reddit"""

import requests


def recurse(subreddit, hot_list=[]):
    """query a subreddit and return a list of titles of hot articles"""

    # Reddit API endpoint for getting subreddit informatiom
    url = 'https://www.reddit.com/r/{}/hot.json'.format(subreddit)

    # Set a custom User-Agent to avoid too many requests error
    headers = {
        'User-Agent':
        'Mozilla/5.0 (Windows; U; Windows NT 5.1; de; rv:1.9.2.3) \
        Gecko/20100401 Firefox/3.6.3 (FM Scene 4.6.1)'
    }

    # send a GET request to the Reddit API
    response = requests.get(url, headers=headers, allow_redirects=False)
    reddits = response.json()

    try:
        children = reddits.get('data').get('children')
        for title in children:
            hot_list.append(title.get('data').get('title'))
        return hot_list
    except Exception:
        print(None)
        return 0
