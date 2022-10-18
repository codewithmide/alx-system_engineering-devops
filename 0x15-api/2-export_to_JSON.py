#!/usr/bin/python3
"""extend your Python script to export data in the JSON format"""
import json
import requests
from sys import argv


if __name__ == "__main__":
    """Your code should not be executed when imported"""

    user_id = argv[1]

    todos = requests.get(
        "http://jsonplaceholder.typicode.com/todos?userId={}".format(
            user_id))
    user = requests.get(
        "http://jsonplaceholder.typicode.com/users/{}".format(
            user_id))

    out = {user.json().get('id'): []}
    with open('{}.csv'.format(user_id), "w") as output:
        for tarea in todos.json():
            data = {
                'task': tarea.get('title'),
                'completed': tarea.get('completed'),
                'username': user.json().get('username')
            }
            out.get(user.json().get('id')).append(data)
        json.dump(out, output)
