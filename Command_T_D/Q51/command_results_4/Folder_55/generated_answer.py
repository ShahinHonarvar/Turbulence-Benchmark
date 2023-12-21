def if_contains_anagrams(s):
    return s.lower() in [a.lower() for a in s if sorted(a) == sorted(b) for b in s if a == b or a == b[::-1]]
