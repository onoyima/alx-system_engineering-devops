#!/usr/bin/python3
"""
Gather data from an API
"""
import requests
import sys

def gather_employee_todo_progress(employee_id):
    """
    Retrieves and displays the employee's TODO list progress.

    Args:
        employee_id (int): The ID of the employee.

    Returns:
        None
    """
    # Fetch user data
    user_url = f"https://jsonplaceholder.typicode.com/users/{employee_id}"
    todos_url = f"https://jsonplaceholder.typicode.com/todos?userId={employee_id}"

    try:
        user_response = requests.get(user_url)
        todos_response = requests.get(todos_url)

        if user_response.status_code != 200 or todos_response.status_code != 200:
            print("Error: Unable to fetch data. Please check the employee ID.")
            return

        user_data = user_response.json()
        todos_data = todos_response.json()

        # Calculate progress
        total_tasks = len(todos_data)
        completed_tasks = [task for task in todos_data if task['completed']]
        num_completed_tasks = len(completed_tasks)
        employee_name = user_data['name']

        # Display progress
        print(f"Employee {employee_name} is done with tasks({num_completed_tasks}/{total_tasks}):")
        for task in completed_tasks:
            print(f"     {task['title']}")

    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: python3 0-gather_data_from_an_API.py <employee_id>")
        sys.exit(1)

    try:
        employee_id = int(sys.argv[1])
    except ValueError:
        print("Error: Employee ID must be an integer.")
        sys.exit(1)

    gather_employee_todo_progress(employee_id)
