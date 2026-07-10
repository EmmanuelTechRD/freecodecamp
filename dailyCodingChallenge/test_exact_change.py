import unittest
from exact_change import exact_change

class TestsWaysToMakeChange(unittest.TestCase):

    def test_three_cents(self):
        self.assertEqual(exact_change(3), 1)
        
    def test_seven_cents(self):
        self.assertEqual(exact_change(7), 2)

    def test_ten_cents(self):
        self.assertEqual(exact_change(10), 4)

    def test_one_dollar(self):
        self.assertEqual(exact_change(100), 242)

if __name__ == '__main__':
    unittest.main()