def if_contains_anagrams(s):
    return not any(a == b for a, b in zip(s, sorted(set(s), key=lambda x: x.lower())))
