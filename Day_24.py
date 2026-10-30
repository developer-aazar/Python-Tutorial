# Day 24 - Python Programming Course

# Today we will cover pathlib, a standard-library module for working with file
# and folder paths in a clear way across different operating systems.

from pathlib import Path

# Path.cwd() is the folder where the program is running.

current_folder = Path.cwd()
print("Current folder:", current_folder)

# A Path can be combined with / to make a path inside another folder.

readme_path = current_folder / "README.md"
print("README path:", readme_path)
print("Does README exist?", readme_path.exists())
print("Is it a file?", readme_path.is_file())
print("File name:", readme_path.name)
print("File extension:", readme_path.suffix)

# glob() finds paths that match a pattern. This example lists Python files in
# the current folder without opening or changing them.

python_files = sorted(current_folder.glob("Day_*.py"))
print("Tutorial day files:")
for path in python_files:
	print(path.name)

# Path.read_text() and Path.write_text() are convenient for small text files.
# For larger files, use open() with a with block as shown in Day 15.

# Day 24 Project: Ask for a file name and display its extension if it exists.

file_name = input("Enter a file name in this folder: ")
chosen_path = current_folder / file_name

if chosen_path.is_file():
	print("File found:", chosen_path.name)
	print("Extension:", chosen_path.suffix or "No extension")
else:
	print("That file was not found in the current folder.")
