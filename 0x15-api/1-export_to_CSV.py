#!/usr/bin/python3
"""exports information to CSV format"""

import requests
import sys
import csv

if __name__ == "__main__":
    # Retrieve user ID from CLI
    user_id = sys.argv[1]

    # Define the URL for the REST API
    url = "https://jsonplaceholder.typicode.com/"

    # send a GET request to retrieve user info
    user = requests.get(url + "users/{}".format(user_id)).json()

    # get the username of the user
    username = user.get("username")

    # send a GET request to retrive the TODO list
    todos = requests.get(url + "todos", params={"userId": user_id}).json()

    # open a CSV file for writing
    with open("{}.csv".format(user_id), "w", newline="") as csvfile:
        writer = csv.writer(csvfile, quoting=csv.QUOTE_ALL)
        [writer.writerow(
            [user_id, username, t.get("completed"), t.get("title")]
        ) for t in todos]
