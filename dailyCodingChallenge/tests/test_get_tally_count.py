import unittest
from get_tally_count import get_tally_count

class TestTallyCounter(unittest.TestCase):

    def test_empty_string(self):
        self.assertEqual(get_tally_count(""), 0)

    def test_incomplete_group(self):
        self.assertEqual(get_tally_count("||/"), 3)

    def test_single_full_group(self):
        self.assertEqual(get_tally_count("||||/"), 5)

    def test_multiple_full_groups(self):
        self.assertEqual(get_tally_count("||||/ ||||/"), 10)

    def test_mixed_groups(self):
        self.assertEqual(get_tally_count("||||/ ||||/ ||"), 12)

    def test_only_spaces(self):
        self.assertEqual(get_tally_count("   "), 0)

if __name__ == '__main__':
    unittest.main()