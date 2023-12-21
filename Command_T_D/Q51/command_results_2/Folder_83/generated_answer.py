def if_contains_anagrams(s):
    return sum(a.lower() == b.lower() for a, b in zip(s, s[1:])) <= 19
