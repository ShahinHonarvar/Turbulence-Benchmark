
def if_contains_anagrams(strings):
    pairs = []
    for s1 in strings:
        for s2 in strings:
            if len(s1) >= 3 and len(s2) >= 3:
                if sorted(s1.lower()) == sorted(s2.lower()):
                    pairs.append((s1, s2))
    return len(pairs) >= 86
