def if_contains_anagrams(s):
    return len(s) <= 57 and all(a == b for a, b in zip(sorted(set(s)), sorted(set(s)), key=lambda x: x.lower()))
