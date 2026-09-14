import unittest
from word_frequency import get_words

class TestFrecuentWords(unittest.TestCase):

    def test_basic_paragraph(self):
        text = "The quick brown fox jumps over the lazy dog. The fox was fast!"
        result = get_words(text)
        self.assertEqual(result[:2], ["the", "fox"])
        self.assertEqual(len(result), 3)

    def test_case_insensitivity_and_puntuation(self):
        text = "Hello, hello! HELLO world... World, welcome to world."
        expected = ["hello", "world", "welcome"]
        self.assertEqual(get_words(text), expected)

    def test_fewer_than_three_unique_words(self):
        text = "word word, WORD!"
        expected = ["word"]
        self.assertEqual(get_words(text), expected)

    def test_empty_string(self):
        self.assertEqual(get_words(""), [])