def if_contains_anagrams(texts):
    return len(texts) <= 29 and len(texts) >= 3 and all(text.lower() in set(texts) for text in texts)
