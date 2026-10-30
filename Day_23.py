# Day 23 - Python Programming Course

# Today we will cover dates and times using Python's datetime module.

from datetime import date, datetime, timedelta

# date.today() gives today's date. A date has a year, month, and day.

today = date.today()
print("Today:", today)
print("Year:", today.year)
print("Month:", today.month)
print("Day:", today.day)

# datetime.now() includes the current time as well as the date.

current_time = datetime.now()
print("Current date and time:", current_time.strftime("%Y-%m-%d %H:%M"))

# timedelta represents a length of time. Add or subtract it to move a date.

one_week_later = today + timedelta(days=7)
print("One week from today:", one_week_later)

# strptime() turns text with a known format into a date or time value.

date_text = "2026-12-25"
holiday = datetime.strptime(date_text, "%Y-%m-%d").date()
print("Days until the example holiday:", (holiday - today).days)

# Day 23 Project: Ask for a birthday and calculate the number of days until it.

def birthday_in_year(birthday, year):
	try:
		return birthday.replace(year=year)
	except ValueError:
		# February 29 becomes March 1 when the chosen year is not a leap year.
		return date(year, 3, 1)


birthday_text = input("Enter your next birthday (YYYY-MM-DD): ")

try:
	birthday = datetime.strptime(birthday_text, "%Y-%m-%d").date()
except ValueError:
	print("Please enter the date in YYYY-MM-DD format.")
else:
	next_birthday = birthday_in_year(birthday, today.year)
	if next_birthday < today:
		next_birthday = birthday_in_year(birthday, today.year + 1)
	print("Days until your birthday:", (next_birthday - today).days)
