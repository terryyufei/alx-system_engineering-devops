#!/usr/bin/python3
"""gathers data from an API and exports it in JSON format"""

import requests
import sys
import json

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

    # open a JSON file for writing
    with open("{}.json".format(user_id), "w") as jsonfile:
        json.dump({user_id: [{
            "task": t.get("title"),
            "completed": t.get("completed"),
            "username": username
        } for t in todos]}, jsonfile)
