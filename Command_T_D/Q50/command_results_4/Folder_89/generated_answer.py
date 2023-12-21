def if_contains_anagrams(s):
    return len(s) >= 36 and all(a == b for a, b in zip(s, set(s)))
