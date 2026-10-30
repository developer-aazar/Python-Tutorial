# Day 15 - Python Programming Course

# Today we will cover reading and writing text files. A file lets your program
# keep information after it finishes running.

# Use with open(...) so Python closes the file automatically when the block ends.
# The w mode writes a new file, replacing its old contents if it already exists.

with open("day15_notes.txt", "w", encoding="utf-8") as file:
	file.write("Python file handling\n")
	file.write("The with statement manages the file for us.\n")

# The r mode reads an existing file. read() returns all of its text.

with open("day15_notes.txt", "r", encoding="utf-8") as file:
	notes = file.read()

print("Notes in the file:")
print(notes)

# The a mode adds text to the end instead of replacing the file.

with open("day15_notes.txt", "a", encoding="utf-8") as file:
	file.write("This line was added later.\n")

# A for loop can read a file one line at a time, which is useful for larger files.

with open("day15_notes.txt", "r", encoding="utf-8") as file:
	for line_number, line in enumerate(file, start=1):
		print(f"Line {line_number}: {line.rstrip()}")

# Day 15 Project: Ask the user for a journal entry and save it to a text file.

journal_entry = input("Write a short journal entry: ")

with open("day15_journal.txt", "a", encoding="utf-8") as file:
	file.write(journal_entry + "\n")

print("Your journal entry was saved.")
