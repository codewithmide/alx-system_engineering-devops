#!/usr/bin/python3
""" a Python script that, using a REST API, for a given employee ID,
    returns information about his/her TODO list progress."""
import requests
import sys


if __name__ == '__main__':
    url = 'https://jsonplaceholder.typicode.com/users/' + sys.argv[1]
    r = requests.get(url)
    name = r.json().get("name")
    url2 = 'https://jsonplaceholder.typicode.com/todos'
    r2 = requests.get(url2)
    task_names = []
    tasks = 0
    completed = 0
    for item in r2.json():
        if item.get("userId") == int(sys.argv[1]):
            tasks += 1
            if item.get("completed") is True:
                completed += 1
                task_names.append(item.get("title"))
    print("Employee {} is done with tasks({}/{}):".format(name,
                                                          completed,
                                                          tasks))
    for i in task_names:
        print("\t {}".format(i))
