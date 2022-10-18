#!/usr/bin/python3
""" a Python script that, using a REST API, for a given employee ID,
    returns information about his/her TODO list progress."""
import json
import requests
import sys


if __name__ == '__main__':
    url = 'https://jsonplaceholder.typicode.com/users?id=' + sys.argv[1]
    r = requests.get(url)
    if r.status_code == 200:
        data = {sys.argv[1]: []}
        username = r.json()[0].get("username")
        url2 = 'https://jsonplaceholder.typicode.com/todos'
        r2 = requests.get(url2)
        for item in r2.json():
            if item.get("userId") == int(sys.argv[1]):
                d = {'task': item.get('title'),
                     'completed': item.get('completed'),
                     'username': username}
                data[sys.argv[1]].append(d)
    filename = sys.argv[1] + '.json'
    with open(filename, 'w') as f:
        json.dump(data, f)
