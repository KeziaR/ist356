from datetime import datetime


today = datetime.now()
print(today)

BDay = input("Enter birthday in the format MM/DD/YYYY: ")

test = datetime.strptime(BDay, "%m/%d/%Y")

testing = test + datetime.timedelta(days = 15)

"Wednesday, January 15, 1990"

test_str = testing.strftime(BDay, "%A, %B %d, %Y")

print(test_str)

