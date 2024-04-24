#!/usr/bin/python3
# script must display on the standard output the employee TODO list progress in this exact format
import json
import urllib.request
url = f"https://jsonplaceholder.typicode.com/users/{employee_id}/todos"
try:
    with urllib.request.urlopen(url) as response:
        data = json.loads(response.read().decode())
        
        completed_tasks = [todo for todo in data if todo['completed']]
        num_completed_tasks = len(completed_tasks)
        total_tasks = len(data)
        
        employee_name = data[0]['name'] if data else "Unknown"
        print(f"Employee {employee_name} is done with tasks ({num_completed_tasks}/{total_tasks}):")
        for task in completed_tasks:
            print(f"\t{task['title']}")
except urllib.error.HTTPError as e:
    print("Failed to fetch TODO list.")
    print(e)
