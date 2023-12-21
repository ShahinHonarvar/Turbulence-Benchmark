def if_contains_anagrams(s):
    return sum(1 for a, b in zip(s, s) if a == b[1:-1]) >= 277
