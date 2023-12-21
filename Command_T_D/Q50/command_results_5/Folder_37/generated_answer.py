def if_contains_anagrams(s):
    return len(s) >= 29 and len(s) % 2 == 0 and all(a == b for a, b in zip(s, s))
