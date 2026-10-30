# Day 29 - Python Programming Course

# Today we will cover context managers. A context manager sets something up,
# runs a block of code, and then reliably performs cleanup.

# The with statement uses a context manager. Files are closed automatically
# when the indented block ends, even if an exception happens inside the block.

with open("day29_example.txt", "w", encoding="utf-8") as file:
	file.write("The with statement manages this file.\n")

with open("day29_example.txt", "r", encoding="utf-8") as file:
	print(file.read().rstrip())

# The threading.Lock class is another context manager. It releases the lock
# after the block so another part of a program can safely use shared data.

from threading import Lock

shared_lock = Lock()

with shared_lock:
	print("The protected section is running.")

# contextmanager lets you create a small context manager using a generator.

from contextlib import contextmanager

@contextmanager
def simple_timer():
	print("Timer started.")
	try:
		yield
	finally:
		print("Timer finished.")


with simple_timer():
	print("Doing a short task.")

# Day 29 Project: Use a context manager around a short study session.

@contextmanager
def study_session(topic):
	print(f"Starting study session: {topic}")
	try:
		yield
	finally:
		print("Study session complete.")


with study_session("Python context managers"):
	print("Reviewing examples...")
