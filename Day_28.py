# Day 28 - Python Programming Course

# Today we will cover SQLite databases with Python's built-in sqlite3 module.
# A database stores structured information in tables.

import sqlite3

# :memory: creates a temporary database that disappears when the program ends.

connection = sqlite3.connect(":memory:")
cursor = connection.cursor()

cursor.execute(
	"CREATE TABLE students (id INTEGER PRIMARY KEY, name TEXT, course TEXT)"
)

# Use ? placeholders for values instead of joining user text into SQL commands.

student_records = [
	("Ali", "Python"),
	("Sara", "Data Science"),
	("Omar", "Python"),
]
cursor.executemany(
	"INSERT INTO students (name, course) VALUES (?, ?)",
	student_records,
)
connection.commit()

# SELECT reads rows from a table. fetchall() returns all matching rows.

cursor.execute("SELECT name, course FROM students ORDER BY name")
for name, course in cursor.fetchall():
	print(f"{name} is studying {course}.")

# A WHERE clause filters rows. Query values still use placeholders.

cursor.execute("SELECT name FROM students WHERE course = ?", ("Python",))
print("Python students:", [row[0] for row in cursor.fetchall()])

connection.close()

# Day 28 Project: Create a small in-memory book table and count its rows.

with sqlite3.connect(":memory:") as connection:
	connection.execute("CREATE TABLE books (title TEXT, author TEXT)")
	connection.executemany(
		"INSERT INTO books VALUES (?, ?)",
		[("Python Basics", "A. Jatoi"), ("Learning Python", "S. Example")],
	)
	book_count = connection.execute("SELECT COUNT(*) FROM books").fetchone()[0]
	print("Books in the database:", book_count)

connection.close()
