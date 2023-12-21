def if_contains_anagrams(s):
    return sum(s) > len(s) // 2 and len(s) > 1 and all(a == b for a, b in zip(s, s))
