from datetime import datetime
from dateutil.relativedelta import relativedelta
import sys

print("Welcome to the date difference calculator!")
print("If you want to see the difference between a date and now, enter 1.")
print("If you want to see the difference between two dates, enter 2.")
choice = input("")

# Expected format
format = "%m/%d/%Y"

# Convert the user input to a datetime object
def time_conversion(input):
    if (datetime.strptime(input, format)):
        return datetime.strptime(input, format)
    else:
        print("Incorrect input value!")
        sys.exit()

if (choice == "1"):
    date1 = time_conversion(input("What is date you'd like to calculate? Please enter in MM/DD/YYYY format. "))
    date2 = datetime.now()
elif (choice == "2"):
    date1 = time_conversion(input("What is the first date you'd like to calculate? Please enter in MM/DD/YYYY format. "))
    date2 = time_conversion(input("What is the second date you'd like to calculate? Please enter in MM/DD/YYYY format. "))
else:
    print("Invalid entry!")
    sys.exit()
    
difference = relativedelta(date1, date2)
years = abs(difference.years)
if (years == 1):
    years_plural = ""
else:
    years_plural = "s"

months = abs(difference.months)
if (months == 1):
    months_plural = ""
else:
    months_plural = "s"
    
days = abs(difference.days)
if (days == 1):
    days_plural = ""
else:
    days_plural = "s"

print(f"The difference is {years} year{years_plural}, {months} month{months_plural}, and {days} day{days_plural}!")