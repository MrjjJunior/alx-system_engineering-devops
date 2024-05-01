#!/usr/bin/python3
"""Gathers data from an API."""
import requests
import sys

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: {} <employee_id>".format(sys.argv[0]))
        sys.exit(1)

    employee_id = sys.argv[1]
    url_user = "https://jsonplaceholder.typicode.com/users/{}".format(employee_id)
    url_todos = "https://jsonplaceholder.typicode.com/todos?userId={}".format(employee_id)

    response_user = requests.get(url_user)
    response_todos = requests.get(url_todos)

    if response_user.status_code != 200:
        print("Error: User data not found")
        sys.exit(1)

    if response_todos.status_code != 200:
        print("Error: Todo data not found")
        sys.exit(1)

    user_data = response_user.json()
    todos_data = response_todos.json()

    total_tasks = len(todos_data)
    completed_tasks = [task for task in todos_data if task['completed']]
    total_completed_tasks = len(completed_tasks)
    employee_name = user_data['name']

    print("Employee {} is done with tasks({}/{}):".format(employee_name, total_completed_tasks, total_tasks))
    for task in completed_tasks:
        print("\t {}".format(task['title']))

