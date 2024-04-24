#!/usr/bin/python3
"""Python script that, using this REST API, for a given employee ID, returns information about his/her TODO list progress."""
import requests
import sys

def get_employee_todo_list_progress(employee_id):
    url = f'https://jsonplaceholder.typicode.com/users/{employee_id}/todos'
    response = requests.get(url)
    data = response.json()

    if not data:
        print(f'No data found for employee with ID {employee_id}.')
        return

    employee_name = data[0]['username']
    done_tasks = [task for task in data if task['completed']]
    total_tasks = len(data)
    num_done_tasks = len(done_tasks)

    print(f'Employee {employee_name} is done with tasks ({num_done_tasks}/{total_tasks}):')

    for task in done_tasks:
        print(f'\t{task["title"]}')

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print('Usage: python script.py <employee_id>')
        sys.exit(1)

    employee_id = int(sys.argv[1])
    get_employee_todo_list_progress(employee_id)
