def if_contains_anagrams(s):
    return s.lower() and set(s) == set(s.lower()) and sum(1 for x, y in zip(s, s) if x == y and len(x) > 2) >= 84
