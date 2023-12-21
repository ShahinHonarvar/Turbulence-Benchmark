def if_contains_anagrams(s):
    return sum(a == b for a, b in zip(s, sorted(set(s), key=lambda c: c.lower()))) >= 41
