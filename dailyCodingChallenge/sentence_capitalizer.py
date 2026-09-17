# freeCodeCamp challenge: Sentence Capitalizer
# Given a paragraph, return a new paragraph where the first letter of each sentence is capitalized.
# All other characters should be preserved.
# Sentences can end with a period (.), one or more question marks (?), or one or more exclamation points (!).
import re

def capitalize(paragraph):
    if not paragraph:
        return paragraph

    pattern = r'(^|[\.\?\!]+[^a-zA-Z]*)([a-zA-Z])'

    def _capitalize(match: re.Match):
        return match.group(1) + match.group(2).upper()

    return re.sub(pattern, _capitalize, paragraph)

print(capitalize("hello world. \"quotes\" here!"))