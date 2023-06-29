
import requests

def get_todo(id):
    response = requests.get(f"https://jsonplaceholder.typicode.com/todos/{id}")
    if response.status_code == 200:
        return response.json()
    return None


