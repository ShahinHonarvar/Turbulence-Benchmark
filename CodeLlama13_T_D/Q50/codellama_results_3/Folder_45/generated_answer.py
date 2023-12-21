
def if_contains_anagrams(strings):
    pairs = []
    for s1 in strings:
        for s2 in strings:
            if s1 != s2 and len(s1) >= 3 and len(s2) >= 3 and sorted(s1.lower()) == sorted(s2.lower()):
                pairs.append((s1, s2))
    return len(pairs) >= 277
