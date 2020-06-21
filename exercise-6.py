# exercise-06 What's the  Season?

# Write the code that:
# 1. Prompts the user to enter the month (as three characters):
#      Enter the month of the year (Jan - Dec):
# 2. Then prompts the user to enter the day of the month: 
#      Enter the day of the month:
# 3. Calculate what season it is based upon this chart:
#      Dec 21 - Mar 19: Winter
#      Mar 20 - Jun 20: Spring
#      Jun 21 - Sep 21: Summer
#      Sep 22 - Dec 20: Fall
# 4. Print the result as follows:
#      <Mmm> <dd> is in <season> 

# Hints:
# Consider using the in operator to check if a string is in a particular list/tuple like this:
# if input_month in ('Jan', 'Feb', 'Mar'):
#
# After setting the likely season, you can use another if...elif...else statement to "adjust" if
# the day number falls within a certain range.

month = input('Enter the month of the year (Jan - Dec): ')
date = int(input('Enter the day of the month: '))

# Write the if...elif...else statement as described in the lesson

if month == "Jan" or month == 'Feb':
    print(f' {month} {date} is in Winter')
elif month == "Dec" and date > 20:
    print(f' {month} {date} is in Winter')
elif month == "Mar" and date < 20:
    print(f' {month} {date} is in Winter')
elif month == "Apr" or month == 'May':
    print(f' {month} {date} is in Spring')
elif month == "Mar" and date > 19:
    print(f' {month} {date} is in Spring')
elif month == "Jun" and date < 21:
    print(f' {month} {date} is in Spring')
elif month == "Jul" or month == 'Aug':
    print(f' {month} {date} is in Summer')
elif month == "Jun" and date > 20:
    print(f' {month} {date} is in Summer')
elif month == "Sep" and date < 22:
    print(f' {month} {date} is in Summer')
elif month == "Oct" or month == 'Nov':
    print(f' {month} {date} is in Fall')
elif month == "Sep" and date > 21:
    print(f' {month} {date} is in Fall')
elif month == "Dec" and date < 21:
    print(f' {month} {date} is in Fall')
