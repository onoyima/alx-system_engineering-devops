import csv
import requests
import sys

def export_todo_to_csv(employee_id):
    # Fetch user data
    user_url = f"https://jsonplaceholder.typicode.com/users/{employee_id}"
    user_response = requests.get(user_url)
    
    if user_response.status_code != 200:
        print(f"Error: Employee with ID {employee_id} not found.")
        return
    
    user_data = user_response.json()
    username = user_data['username']
    
    # Fetch todos data for the user
    todos_url = f"https://jsonplaceholder.typicode.com/todos?userId={employee_id}"
    todos_response = requests.get(todos_url)
    
    if todos_response.status_code != 200:
        print(f"Error: Could not retrieve TODO list for employee with ID {employee_id}.")
        return
    
    todos_data = todos_response.json()
    
    # Prepare CSV file
    csv_filename = f"{employee_id}.csv"
    with open(csv_filename, mode='w', newline='') as csv_file:
        csv_writer = csv.writer(csv_file, quoting=csv.QUOTE_ALL)
        
        # Write CSV header and rows
        for task in todos_data:
            csv_writer.writerow([employee_id, username, task['completed'], task['title']])
    
    print(f"Data for employee {username} (ID: {employee_id}) has been exported to {csv_filename}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 1-export_to_CSV.py <employee_id>")
        sys.exit(1)
    
    try:
        employee_id = int(sys.argv[1])
    except ValueError:
        print("Error: Employee ID must be an integer.")
        sys.exit(1)
    
    export_todo_to_csv(employee_id)

