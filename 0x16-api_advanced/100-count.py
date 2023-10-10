#!/usr/bin/python3
"""Contains the count_words function"""

import requests


def count_words(subreddit, word_list, found_list=[], after=None):
    """
    recursive function that queries the Reddit API, parses the title of
    all hot articles, and prints a sorted count of given keywords
    """

    # Send a GET request to the Reddit API for hot posts
    posts = requests.get('http://www.reddit.com/r/{}/hot.json?after={}'
                         .format(subreddit, after), headers=user_agent)

    # Set a custom User-Agent to avoid Too Many Requests error
    user_agent = {'User-agent': 'test45'}

    # If it's the initial call, convert all words in the word_list to lowercase
    if after is None:
        word_list = [word.lower() for word in word_list]

    if posts.status_code == 200:
        # Parse the JSON response to access post data and 'after' parameter
        posts = posts.json()['data']
        aft = posts['after']
        posts = posts['children']

    # Loop through the posts and check for keywords in their titles
    for post in posts:
        title = post['data']['title'].lower()
        for word in title.split(' '):
            if word in word_list:
                found_list.append(word)

    # If there's a next page, make a recursive call with 'after' parameter
    if aft is not None:
        count_words(subreddit, word_list, found_list, aft)
    else:
        # Count the occurrences of each keyword and print the results
        result = {}
        for word in found_list:
            if word.lower() in result.keys():
                result[word.lower()] += 1
            else:
                result[word.lower()] = 1
        for key, value in sorted(result.items(), key=lambda item: item[1],
                                 reverse=True):
            print('{}: {}'.format(key, value))
    else:
        return  # Return None for invalid subreddits or other errors
