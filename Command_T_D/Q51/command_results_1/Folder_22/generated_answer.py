def if_contains_anagrams(s):
    return not any(a == b for a, b in zip(s, set(s)) if a == b.lower() and len(a) >= 3)
