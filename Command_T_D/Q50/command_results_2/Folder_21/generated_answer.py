def if_contains_anagrams(s):
    return sum(1 for x, y in zip(s, s) if len(x) >= 3 and len(y) >= 3 and set(x.lower()) == set(y.lower())) >= 136
