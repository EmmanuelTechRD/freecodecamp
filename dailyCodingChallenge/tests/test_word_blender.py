import unittest
from word_blender import blend_words

class TestWordBlender(unittest.TestCase):
    def test_even_length_words(self):
        word1 = "turtle"
        word2 = "toucan"

        expected = "turcan"
        self.assertEqual(blend_words(word1, word2), expected)

    def test_odd_length_words(self):
        word1 = "apple"
        word2 = "juice"

        expected = "apice"
        self.assertEqual(blend_words(word1, word2), expected)

    def test_odd_and_even_mix(self):
        word1 = "car"
        word2 = "home"

        expected = "cme"
        self.assertEqual(blend_words(word1, word2), expected)

    def test_even_and_odd_mix(self):
        word1 = "buying"
        word2 = "selling"

        expected = "buyling"
        self.assertEqual(blend_words(word1, word2), expected)

    def test_single_character_words(self):
        word1 = "x"
        word2 = "y"

        expected = "y"
        self.assertEqual(blend_words(word1, word2), expected)