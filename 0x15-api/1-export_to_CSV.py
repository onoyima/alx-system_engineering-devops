#!/usr/bin/python3
"""Export API to CSV"""
import csv
import requests
import sys

def export_todo_to_csv(user_id):
    # Define the URLs
    url_user = f'https://jsonplaceholder.typicode.com/users/{user_id}'
    url_todos = f'https://jsonplaceholder.typicode.com/users/{user_id}/todos'

    # Fetch user data
    response_user = requests.get(url_user)
    if response_user.status_code != 200:
        print(f"Error: Unable to fetch user data for user ID {user_id}.")
        return
    
    user_data = response_user.json()
    username = user_data.get('username')

    # Fetch todos data
    response_todos = requests.get(url_todos)
    if response_todos.status_code != 200:
        print(f"Error: Unable to fetch todos for user ID {user_id}.")
        return
    
    todos_data = response_todos.json()

    # Create CSV file
    csv_filename = f'{user_id}.csv'
    with open(csv_filename, mode='w', newline='', encoding='utf-8') as csvfile:
        csv_writer = csv.writer(csvfile, quoting=csv.QUOTE_ALL)
        csv_writer.writerow(["USER_ID", "USERNAME", "TASK_COMPLETED_STATUS", "TASK_TITLE"])
        for task in todos_data:
            csv_writer.writerow([
                user_id,
                username,
                task.get('completed'),
                task.get('title')
            ])
    print(f"Data for user {username} (ID: {user_id}) has been exported to {csv_filename}")

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: python3 1-export_to_CSV.py <user_id>")
        sys.exit(1)
    
    user_id = sys.argv[1]
    export_todo_to_csv(user_id)

