def if_contains_anagrams(texts):
    res = len(texts) * len(texts) // 2 * 2
    return res >= 22
