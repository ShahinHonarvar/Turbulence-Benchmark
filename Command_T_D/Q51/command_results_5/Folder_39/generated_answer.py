def if_contains_anagrams(texts):
    return all(c.lower() == b.lower() for b, c in zip(texts, texts))
