#!/usr/bin/python3
import requests
import sys

def get_employee_todo_progress(employee_id):
    # Fetch user data
    user_url = f"https://jsonplaceholder.typicode.com/users/{employee_id}"
    user_response = requests.get(user_url)

    if user_response.status_code != 200:
        print(f"Error: Employee with ID {employee_id} not found.")
        return

    user_data = user_response.json()
    employee_name = user_data['name']

    # Fetch todos data for the user
    todos_url = f"https://jsonplaceholder.typicode.com/todos?userId={employee_id}"
    todos_response = requests.get(todos_url)

    if todos_response.status_code != 200:
        print(f"Error: Could not retrieve TODO list for employee with ID {employee_id}.")
        return

    todos_data = todos_response.json()

    # Calculate the number of done tasks and total tasks
    total_tasks = len(todos_data)
    done_tasks = [task for task in todos_data if task['completed']]
    number_of_done_tasks = len(done_tasks)

    # Display the results
    print(f"Employee {employee_name} is done with tasks({number_of_done_tasks}/{total_tasks}):")
    for task in done_tasks:
        print(f"\t {task['title']}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 0-gather_data_from_an_API.py <employee_id>")
        sys.exit(1)

    try:
        employee_id = int(sys.argv[1])
    except ValueError:
        print("Error: Employee ID must be an integer.")
        sys.exit(1)

    get_employee_todo_progress(employee_id)

