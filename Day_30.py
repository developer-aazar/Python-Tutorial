# Day 30 - Python Programming Course

# Today we will build a small command-line task list. This capstone combines
# functions, lists, loops, conditions, exceptions, and JSON file storage.

import json
from pathlib import Path

TASKS_FILE = Path("day30_tasks.json")


def load_tasks():
	"""Load saved tasks, or return an empty list when no file exists yet."""
	if not TASKS_FILE.exists():
		return []

	try:
		with TASKS_FILE.open("r", encoding="utf-8") as file:
			tasks = json.load(file)
	except (json.JSONDecodeError, OSError):
		print("Could not read the saved task list. Starting with an empty list.")
		return []

	if not isinstance(tasks, list):
		print("The saved task data is not a list. Starting with an empty list.")
		return []
	return tasks


def save_tasks(tasks):
	"""Write the task list to a JSON file."""
	with TASKS_FILE.open("w", encoding="utf-8") as file:
		json.dump(tasks, file, indent=4)


def show_tasks(tasks):
	"""Print all tasks with their completion status."""
	if not tasks:
		print("Your task list is empty.")
		return

	for task_number, task in enumerate(tasks, start=1):
		status = "done" if task["done"] else "not done"
		print(f"{task_number}. [{status}] {task['title']}")


def main():
	tasks = load_tasks()

	while True:
		print("\nTask List")
		print("1. Show tasks")
		print("2. Add a task")
		print("3. Mark a task done")
		print("4. Delete a task")
		print("5. Save and quit")
		choice = input("Choose an option: ").strip()

		if choice == "1":
			show_tasks(tasks)
		elif choice == "2":
			title = input("Enter the task: ").strip()
			if title:
				tasks.append({"title": title, "done": False})
				print("Task added.")
			else:
				print("A task cannot be empty.")
		elif choice in ("3", "4"):
			show_tasks(tasks)
			try:
				task_number = int(input("Enter the task number: "))
			except ValueError:
				print("Please enter a whole number.")
				continue

			if not 1 <= task_number <= len(tasks):
				print("That task number does not exist.")
			elif choice == "3":
				tasks[task_number - 1]["done"] = True
				print("Task marked done.")
			else:
				removed_task = tasks.pop(task_number - 1)
				print(f"Deleted: {removed_task['title']}")
		elif choice == "5":
			save_tasks(tasks)
			print(f"Tasks saved to {TASKS_FILE}.")
			break
		else:
			print("Choose an option from 1 to 5.")


if __name__ == "__main__":
	main()
