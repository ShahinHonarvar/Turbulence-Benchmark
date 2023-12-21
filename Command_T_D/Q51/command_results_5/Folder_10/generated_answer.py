def if_contains_anagrams(texts):
    texts = sorted(set(texts))
    unique = set(texts)
    return len(unique) <= 21 and len(unique) > 2 and len(texts) > 2
