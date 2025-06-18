from task import Task
from utils import load_tasks, save_tasks, generate_task_id
from datetime import datetime, date

def main():
   tasks = load_tasks()

   while True:
      print("\n=== TaskTamer CLI ===")
      print("1. Add Task")
      print("2. List Tasks")
      print("3. Complete Task")
      print("4. Delete Task")
      print("5. Exit")

      choice = input("Choose an option: ")

      if choice == "1":
         add_task(tasks)
      elif choice == "2":
         list_tasks(tasks)
      elif choice == "3":
         complete_task(tasks)
      elif choice == "4":
         delete_task(tasks)
      elif choice == "5":
         save_tasks(tasks)
         print("Goodbye!")
         break
      else:
         print("Invalid choice. Please try again.")

def add_task(tasks):
   title = input("Enter task title: ")
   description = input("Enter task description: ")
   due_date = input("Enter due date (YYYY-MM-DD) [optional]: ")

   task_id = generate_task_id(tasks)
   task = Task(task_id, title, description, due_date if due_date else None)
   tasks.append(task)
   save_tasks(tasks)
   print("Task added!")

def list_tasks(tasks):
   if not tasks:
      print("No tasks found.")
   for task in tasks:
      print(task)

def complete_task(tasks):
   task_id = input("Enter task ID to mark complete: ")
   for task in tasks:
      if str(task.id) == task_id:
         task.mark_complete()
         save_tasks(tasks)
         print("Task marked as complete.")
         return
   print("Task not found.")

def delete_task(tasks):
   task_id = input("Enter task ID to delete: ")
   for task in tasks:
      if str(task.id) == task_id:
         tasks.remove(task)
         save_tasks(tasks)
         print("Task deleted.")
         return
   print("Task not found.")

if __name__ == "__main__":
   main()
