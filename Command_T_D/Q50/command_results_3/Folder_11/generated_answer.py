def if_contains_anagrams(s):
    return len(s) >= 28 and sum(1 for s1, s2 in zip(s, s) if all(a == b for a, b in zip(s1, s2))) >= 28
