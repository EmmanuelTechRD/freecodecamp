import unittest
from birthday_countdown import days_until_birthday

class TestBirthdayCountdown(unittest.TestCase):

    def test_birthday_later_this_year(self):
        # there are 53 days between July 17 and September 8 (in 2026):
        self.assertEqual(days_until_birthday("2026-07-17", "9/8"), 53)

    def test_birthday_already_passed_this_year(self):
        # birthday was in February. today is July. needs to look at 2027:
        self.assertEqual(days_until_birthday("2026-07-20", "2/14"), 209)

    def test_today_is_birthday(self):
        # it returns the days until next year's birthday, not 0:
        self.assertEqual(days_until_birthday("2026-07-20", "7/20"), 365)

    def test_today_is_birthday_crossing_leap_year(self):
        # let's say today is April 1st, 2023 and for your next birthday you need to wait a whole year...
        # since 2024 is a leap year, it contains Feb 29, making it a 366-day wait:
        self.assertEqual(days_until_birthday("2023-04-01", "4/1"), 366)

    def test_leap_day_birthday_on_leap_year(self):
        # born on Feb 29. today is February 20, 2024 (leap year). next birthday is in 9 days:
        self.assertEqual(days_until_birthday("2024-02-20", "2/29"), 9)

    def test_leap_day_birthday_waiting_four_years(self):
        # let's say it is February 29, 2024, as this is a leap year, your next literal birthday date will be on February 29, 2028:
        self.assertEqual(days_until_birthday("2024-02-29", "2/29"), 1461)

if __name__ == '__main__':
    unittest.main()