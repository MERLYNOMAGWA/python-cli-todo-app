import unittest
import os
import json
from utils import load_tasks, save_tasks, generate_task_id
from task import Task

class TestUtils(unittest.TestCase):
   def test_generate_task_id_empty(self):
      tasks = []
      new_id = generate_task_id(tasks)
      self.assertEqual(new_id, 1)

   def test_generate_task_id_with_tasks(self):
      tasks = [Task(1, "Test", "Desc"), Task(2, "Test2", "Desc2")]
      new_id = generate_task_id(tasks)
      self.assertEqual(new_id, 3)
      
   def test_save_and_load_tasks(self):
      test_file = "test_tasks.json"

      original_tasks = [
         Task(1, "Test Task", "This is a test", "2025-06-20", False)
      ]

      save_tasks(original_tasks, test_file)

      loaded_tasks = load_tasks(test_file)

      os.remove(test_file)

      self.assertEqual(len(loaded_tasks), 1)
      self.assertEqual(loaded_tasks[0].id, 1)
      self.assertEqual(loaded_tasks[0].title, "Test Task")
      self.assertEqual(loaded_tasks[0].completed, False)
      
if __name__ == '__main__':
         unittest.main()



