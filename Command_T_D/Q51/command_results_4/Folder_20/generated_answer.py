def if_contains_anagrams(s):
    return not set(a for s1, s2 in zip(s, s) for a in set(s1.lower()) if s2.lower() == a * 2) & {*s, ''.join(sorted(a)) for a in set(s) if len(a) >= 3}
