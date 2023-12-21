def if_contains_anagrams(text):
    return not any(a == b for a, b in zip(text, text))
