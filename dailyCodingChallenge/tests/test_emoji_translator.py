import unittest
from emoji_translator import get_emoji_phrase

class TestEmojiTranslator(unittest.TestCase):

    def test_single_emoji(self):
        self.assertEqual(get_emoji_phrase("🦈"), "shark")

    def test_multiple_emojis(self):
        self.assertEqual(get_emoji_phrase("🦈🍲🧊"), "shark soup ice")

    def test_repeated_emojis(self):
        self.assertEqual(get_emoji_phrase("🧊🧊🥵🥵"), "ice ice hot hot")

    def test_full_table_sequence(self):
        emojis = "👶🐱🐕🐟🥵🧊🪨🦈🍲⭐"
        expected = "baby cat dog fish hot ice rock shark soup star"
        self.assertEqual(get_emoji_phrase(emojis), expected)

    def test_empty_string(self):
        self.assertEqual(get_emoji_phrase(""), "")