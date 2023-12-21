def if_contains_anagrams(s):
    s = sorted(s)
    return (len(s) < 100 and len(s[0]) >= 3 and len(s[1]) >= 3 and
            all(a.lower() == b.lower() for a, b in zip(s, s[1:])))
