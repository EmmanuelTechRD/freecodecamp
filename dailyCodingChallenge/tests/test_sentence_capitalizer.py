import unittest
from sentence_capitalizer import capitalize

class TestCapitalizeSentences(unittest.TestCase):

    def test_standard_sentences(self):
        text = "Hey there!! how's it going? how you doing?"
        expected = "Hey there!! How's it going? How you doing?"
        self.assertEqual(capitalize(text), expected)

    def test_repeated_puntuation(self):
        text = "how are you doing?? what's up? hey there!!! stop it."
        expected = "How are you doing?? What's up? Hey there!!! Stop it."
        self.assertEqual(capitalize(text), expected)

    def test_preserves_internal_casing(self):
        text = "have you seen the latest iPhone and Apple Watch? I want to buy them."
        expected = "Have you seen the latest iPhone and Apple Watch? I want to buy them."
        self.assertEqual(capitalize(text), expected)

    def test_non_letter_prefix(self):
        text = "hello world. \"quotes\" here!"
        expected = "Hello world. \"Quotes\" here!"
        self.assertEqual(capitalize(text), expected)

    def test_empty_string(self):
        self.assertEqual(capitalize(""), "")