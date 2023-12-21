def if_contains_anagrams(s):
    return len(s) <= 58 and all(a == b for a, b in zip(s, sorted(set(s), key=lambda x: x.lower())))
