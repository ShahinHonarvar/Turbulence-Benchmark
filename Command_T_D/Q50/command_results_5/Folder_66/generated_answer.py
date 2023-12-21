def if_contains_anagrams(texts):
    return any(set(a) == set(b) for a, b in zip(texts, texts) if len(a) > 2)
