# imports datetime class from datetime module
from datetime import datetime

class Task:
    """a class that represent a to-do task."""
    
    def __init__(self, task_id, title, description, due_date=None, completed=False):
        
        """Initialize a new Task instance.

        Args:
            task_id (int): Unique identifier for the task.
            title (str): Title of the task.
            description (str): Task description.
            due_date (str, optional): Due date in 'YYYY-MM-DD' format.
            completed (bool, optional): Whether the task is completed."""

        self.id = task_id #Saves the task title to the title attribute.
        self.title = title
        self.description = description
        self.due_date = due_date
        self.completed = completed

    def mark_complete(self):
        """Mark the task as completed."""
        self.completed = True

    def to_dict(self):
        """Convert the task object to a dictionary for saving to JSON.
        Returns:
            dict: Task data as a dictionary."""
        return {
            "id": self.id,
            "title": self.title,
            "description": self.description,
            "due_date": self.due_date,
            "completed": self.completed
        }

    def __str__(self):
        """Human-readable string representation of the task.
        Returns:
            str: Formatted string for the task."""
        status = "✔️ Done" if self.completed else "❗ Pending"
        due = f"(Due: {self.due_date})" if self.due_date else ""
        return f"[{self.id}] {self.title} - {status} {due}\n    {self.description}"
