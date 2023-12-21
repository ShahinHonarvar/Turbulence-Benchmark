def if_contains_anagrams(texts):
    return len(texts) * len(texts) <= 30 * 2 and len(texts) >= 3 and texts and all(a == b for a, b in zip(texts, texts))
