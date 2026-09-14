# freeCodeCamp challenge: Word Frequency
# Given a paragraph, return an array of the three most frequently occurring words.
# Words in the paragraph will be separated by spaces.
# Ignore case in the given paragraph. For example, treat Hello and hello as the same word.
# Ignore punctuation in the given paragraph. Punctuation consists of commas (,), periods (.), and exclamation points (!).
# The returned array should have all lowercase words.
# The returned array should be in descending order with the most frequently occurring word first.
from collections import Counter
from typing import List

def get_words(paragraph):
    cleaned_text = paragraph.lower()
    for char in [",", ".", "!"]:
        cleaned_text = cleaned_text.replace(char, "")

    words = cleaned_text.split()

    counts = Counter(words)
    top_three_words = counts.most_common(3)

    return [word for word, count in top_three_words]