def if_contains_anagrams(texts):
    return bool(set(texts).intersection(texts).count(texts))
