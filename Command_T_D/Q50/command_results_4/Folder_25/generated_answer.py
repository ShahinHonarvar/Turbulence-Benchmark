def if_contains_anagrams(text):
    return bool(text) and len(set(text)) >= 14 and len(set(x for x in text if len(x) >= 3)) >= 14
