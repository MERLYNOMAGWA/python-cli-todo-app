
import json
import os
from task import Task

def load_tasks(file_path="tasks.json"):
    """
    Load tasks from a JSON file and return a list of Task objects.
    """
    tasks = []
    if os.path.exists(file_path):
        try:
            with open(file_path, "r") as f:
                data = json.load(f)
                for item in data:
                    task = Task(
                        task_id=item["id"],
                        title=item["title"],
                        description=item["description"],
                        due_date=item.get("due_date"),
                        completed=item.get("completed", False)
                    )
                    tasks.append(task)
        except (json.JSONDecodeError, IOError) as e:
            print(f"Error loading tasks: {e}")
    return tasks

def save_tasks(tasks, file_path="tasks.json"):
    """
    Save a list of Task objects to a JSON file.
    """
    try:
        with open(file_path, "w") as f:
            json.dump([task.to_dict() for task in tasks], f, indent=4)
    except IOError as e:
        print(f"Error saving tasks: {e}")

def generate_task_id(tasks):
    """
    Generate a unique task ID based on the existing list of tasks.
    """
    if not tasks:
        return 1
    return max(task.id for task in tasks) + 1
