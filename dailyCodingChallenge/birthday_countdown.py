# freeCodeCamp challenge: Birthday Countdown
# Given today's date and a birthday, return the number of days until the person's next birthday.
# Today's date is given as a string in "YYYY-MM-DD" format, with leading zeros, for example: "2026-07-16".
# The birthday is given as a string in "M/D" format, without leading zeros, for example: "9/7".
# If today is their birthday, return the number of days until their next birthday (not 0).
# Leap years should be accounted for.

import datetime

def days_until_birthday(today, birthday):

    # parsing today's date (expects "YYYY-MM-DD")
    today = datetime.date.fromisoformat(today)

    # parsing the birthday month and day (expects "M/D")
    b_month, b_day = map(int, birthday.split('/'))

    # start checking from the current year
    test_year = today.year

    while True:
        try:
            # creating a valid date for the birthday in the test_year
            b_date = datetime.date(test_year, b_month, b_day)

            # the next birthday must be strictly in the future
            if b_date > today:
                return (b_date - today).days
            else:
                test_year += 1
            
        except ValueError:
            # this handles Feb 29 birthdays on non-leap years.
            # datetime.date() throws a ValueError, so we safely skip to the next year.
            pass
        
            test_year += 1