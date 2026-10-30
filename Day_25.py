# Day 25 - Python Programming Course

# Today we will cover CSV files. CSV stands for comma-separated values and is
# often used to exchange tables with spreadsheet programs.

import csv

students = [
	["name", "score"],
	["Ali", 88],
	["Sara", 94],
	["Omar", 79],
]

# newline="" avoids extra blank lines on some systems. utf-8 supports many
# writing systems and special characters.

with open("day25_scores.csv", "w", newline="", encoding="utf-8") as file:
	writer = csv.writer(file)
	writer.writerows(students)

# csv.reader() reads each row as a list of text values.

with open("day25_scores.csv", "r", newline="", encoding="utf-8") as file:
	reader = csv.reader(file)
	for row in reader:
		print(row)

# DictReader() uses the first row as column names, which makes each row easier
# to understand by giving values descriptive keys.

with open("day25_scores.csv", "r", newline="", encoding="utf-8") as file:
	reader = csv.DictReader(file)
	for row in reader:
		print(f"{row['name']} scored {row['score']}.")

# Day 25 Project: Ask for a student's name and score, then add a row to the CSV.

student_name = input("Enter a student's name: ")
student_score = input("Enter the student's score: ")

with open("day25_scores.csv", "a", newline="", encoding="utf-8") as file:
	writer = csv.writer(file)
	writer.writerow([student_name, student_score])

print("Student saved to day25_scores.csv.")
