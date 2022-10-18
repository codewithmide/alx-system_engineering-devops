#!/usr/bin/python3
"""extend your Python script to export data in the JSON format"""
import json
import requests
from sys import argv


if __name__ == "__main__":
    """Your code should not be executed when imported"""

    users = requests.get('{}/users'.format(
        'https://jsonplaceholder.typicode.com')).json()
    tasks = requests.get(
        '{}/todos'.format('https://jsonplaceholder.typicode.com')).json()

    out = dict()

    for user in users:
        out.update({user.get('id'): []})
        for tarea in tasks:
            if tarea.get('userId') == user.get('id'):
                data = {
                        'task': tarea.get('title'),
                        'completed': tarea.get('completed'),
                        'username': user.get('username')
                }
                out.get(user.get('id')).append(data)

    with open('todo_all_employees.json', "w") as file:
        json.dump(out, file)
