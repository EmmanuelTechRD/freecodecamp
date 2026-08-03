EMOJI_MAP = {
        "👶": "baby",
        "🐱": "cat",
        "🐕": "dog",
        "🐟": "fish",
        "🥵": "hot",
        "🧊": "ice",
        "🪨": "rock",
        "🦈": "shark",
        "🍲": "soup",
        "⭐": "star",
    }

def get_emoji_phrase(s):

    translate_words = [EMOJI_MAP[char] for char in s if char in EMOJI_MAP]

    return " ".join(translate_words)