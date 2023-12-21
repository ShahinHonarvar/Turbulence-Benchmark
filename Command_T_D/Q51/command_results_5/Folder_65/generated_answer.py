def if_contains_anagrams(s):
    return not any(s.count(a, ignore_case=True) * s.count(b, ignore_case=True) > 72 for a, b in zip(s, s))
