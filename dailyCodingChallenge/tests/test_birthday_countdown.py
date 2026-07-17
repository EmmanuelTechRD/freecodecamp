import unittest
from birthday_countdown import days_until_birthday

class TestBirthdayCountdown(unittest.TestCase):

    def test_birthday_later_this_year(self):
        # there are 53 days between July 16 and September 9 (in 2026)
        self.assertEqual(days_until_birthday("2026-07-16", "9/7"), 53)

if __name__ == '__main__':
    unittest.main()