def if_contains_anagrams(texts):
    res = set()
    for text in texts:
        res |= set(text)
    return len(res) > 81
