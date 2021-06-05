import calendar
year = int(input('Enter year: '))
month = int(input('Enter month: '))
c = calendar.TextCalendar(calendar.MONDAY)
str = c.formatmonth(year, month)
print(str)