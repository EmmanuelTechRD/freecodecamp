import unittest
from food_chain import get_food_chain

class TestFoodChain(unittest.TestCase):

    def test_simple_chain(self):
        pairs = [["wolf", "deer"], ["deer", "grass"]]
        expected = ["wolf", "deer", "grass"]
        self.assertEqual(get_food_chain(pairs), expected)

    def test_unordered_input(self):
        pairs = [["fox", "rabbit"], ["rabbit", "carrots"], ["bear", "fox"]]
        expected = ["bear", "fox", "rabbit", "carrots"]
        self.assertEqual(get_food_chain(pairs), expected)

    def test_longer_chain(self):
        pairs = [
            ["snake", "frog"],
            ["frog", "fly"],
            ["fly", "algae"],
            ["hawk", "snake"],
        ]
        expected = ["hawk", "snake", "frog", "fly", "algae"]
        self.assertEqual(get_food_chain(pairs), expected)

    def test_single_pair(self):
        pairs = [["cat", "mouse"]]
        expected = ["cat", "mouse"]
        self.assertEqual(get_food_chain(pairs), expected)

    def test_empty_string(self):
        self.assertEqual(get_food_chain([]), [])